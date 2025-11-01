"""
Command-line interface for Mutest mutation testing tool.
Provides easy-to-use commands for running mutation tests and generating reports.
"""
import click
import sys
import os
from pathlib import Path
from mutest001 import MutantGenerator, MutationTestExecutor
from report import generate_text_report, generate_html_report, generate_json_report


@click.group()
@click.version_option(version='0.0.1', prog_name='Mutest')
def cli():
    """
    🧬 Mutest - Mutation Testing Tool

    A mutation testing tool that helps evaluate the quality of your test suites
    by introducing small changes (mutations) to your code and checking if your
    tests can detect them.
    """
    pass


@cli.command()
@click.argument('source_file', type=click.Path(exists=True))
@click.argument('test_command')
@click.option('--report-format', '-f',
              type=click.Choice(['text', 'html', 'json', 'all'], case_sensitive=False),
              help='Output format for the report (if not specified, you will be prompted)')
@click.option('--output', '-o',
              type=click.Path(),
              help='Output file path (auto-generated if not specified)')
@click.option('--verbose', '-v', is_flag=True,
              help='Show detailed output during mutation testing')
def run(source_file, test_command, report_format, output, verbose):
    """
    Run mutation tests on a source file.

    SOURCE_FILE: Path to the Python source file to mutate

    TEST_COMMAND: Command to run tests (e.g., "pytest tests/")

    Examples:

        mutest run math_utils.py "pytest tests/test_math.py"

        mutest run src/calculator.py "python -m pytest tests/" --report-format html

        mutest run utils.py "pytest" -f json -o results.json
    """
    click.echo("=" * 60)
    click.echo(click.style("MUTEST - Mutation Testing", fg='cyan', bold=True))
    click.echo("=" * 60)
    click.echo()

    # Create reports directory if it doesn't exist
    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)

    # If format not specified, prompt user
    if not report_format:
        click.echo("Select report format:")
        click.echo("  1. text  - Plain text report")
        click.echo("  2. html  - Interactive HTML report")
        click.echo("  3. json  - Machine-readable JSON report")
        click.echo("  4. all   - Generate all formats")
        click.echo()
        report_format = click.prompt(
            'Choose format',
            type=click.Choice(['text', 'html', 'json', 'all'], case_sensitive=False),
            default='html'
        )
        click.echo()

    # Display configuration
    click.echo(f"Source file: {click.style(source_file, fg='green')}")
    click.echo(f"Test command: {click.style(test_command, fg='green')}")
    click.echo(f"Report format: {click.style(report_format, fg='green')}")
    click.echo()

    # Read source code
    try:
        with open(source_file, 'r') as f:
            source_code = f.read()
    except Exception as e:
        click.echo(click.style(f"Error reading file: {e}", fg='red'), err=True)
        sys.exit(1)

    # Generate mutants
    click.echo(click.style("Generating mutants...", fg='yellow'))
    generator = MutantGenerator()
    mutants = generator.generate_mutants(source_code)
    click.echo(click.style(f"Generated {len(mutants)} mutants", fg='green'))
    click.echo()

    if len(mutants) == 0:
        click.echo(click.style("No mutations found. The source file may not have mutable operators.", fg='yellow'))
        sys.exit(0)

    # Run mutation tests
    executor = MutationTestExecutor(source_file, test_command)

    if verbose:
        click.echo(click.style("Running mutation tests (verbose mode)...", fg='yellow'))

    results = executor.run_mutation_tests(mutants)

    if not results:
        click.echo(click.style("Mutation testing failed. See errors above.", fg='red'), err=True)
        sys.exit(1)

    # Display quick summary
    click.echo()
    click.echo("=" * 60)
    click.echo(click.style("QUICK SUMMARY", fg='cyan', bold=True))
    click.echo("=" * 60)
    click.echo(f"Total Mutants: {results['total']}")
    click.echo(click.style(f"Killed: {results['killed_count']}", fg='green'))
    click.echo(click.style(f"Survived: {results['survived_count']}", fg='red' if results['survived_count'] > 0 else 'green'))
    click.echo(f"Timeout: {results['timeout_count']}")

    score = results['mutation_score']
    score_color = 'green' if score >= 80 else 'yellow' if score >= 60 else 'red'
    click.echo()
    click.echo(f"Mutation Score: {click.style(f'{score:.2f}%', fg=score_color, bold=True)}")
    click.echo()

    # Generate reports
    if report_format in ['text', 'all']:
        output_file = output or 'reports/mutest_report.txt'
        generate_text_report(results, output_file, source_file, test_command)
        click.echo(f"Text report saved: {click.style(output_file, fg='green')}")

    if report_format in ['html', 'all']:
        output_file = output or 'reports/mutest_report.html'
        generate_html_report(results, output_file, source_file, test_command)
        click.echo(f"HTML report saved: {click.style(output_file, fg='green')}")

    if report_format in ['json', 'all']:
        output_file = output or 'reports/mutest_report.json'
        generate_json_report(results, output_file, source_file, test_command)
        click.echo(f"JSON report saved: {click.style(output_file, fg='green')}")

    click.echo()

    # Exit with appropriate code
    if results['survived_count'] > 0:
        click.echo(click.style("Some mutants survived. Consider improving your tests!", fg='yellow'))
        sys.exit(0)  # Don't fail CI/CD, just warn
    else:
        click.echo(click.style("All mutants killed! Great test coverage!", fg='green', bold=True))
        sys.exit(0)


@cli.command()
@click.argument('source_file', type=click.Path(exists=True))
def preview(source_file):
    """
    Preview mutations without running tests.

    Shows all possible mutations that would be generated for a source file.

    Example:

        mutest preview math_utils.py
    """
    click.echo("=" * 60)
    click.echo(click.style("MUTATION PREVIEW", fg='cyan', bold=True))
    click.echo("=" * 60)
    click.echo()

    try:
        with open(source_file, 'r') as f:
            source_code = f.read()
    except Exception as e:
        click.echo(click.style(f"❌ Error reading file: {e}", fg='red'), err=True)
        sys.exit(1)

    generator = MutantGenerator()
    mutants = generator.generate_mutants(source_code)

    click.echo(f"Found {click.style(str(len(mutants)), fg='green', bold=True)} possible mutations:")
    click.echo()

    for i, mutant in enumerate(mutants, 1):
        info = mutant['info']
        click.echo(f"{i}. {click.style(info['type'], fg='yellow')}")
        click.echo(f"   Line {info['line']}: {click.style(info['original'], fg='red')} → {click.style(info['mutated'], fg='green')}")
        click.echo()


if __name__ == "__main__":
    cli()
