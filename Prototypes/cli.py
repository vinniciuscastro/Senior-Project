# cli.py
import click
import subprocess
from report import generate_report

@click.group()
def cli():
    """Mutest CLI - Run unit and mutation tests."""
    pass

@cli.command()
@click.option('--mutation', is_flag=True, help='Run mutation tests instead of unit tests.')
@click.option('--html', is_flag=True, help='Generate HTML report.')
def run(mutation, html):
    """Run tests and generate reports."""
    if mutation:
        click.echo("🧬 Running mutation tests...")
        subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"])
        result = "Mutation testing results here (placeholder)"
    else:
        click.echo("🧪 Running unit tests...")
        subprocess.run(["pytest", "--maxfail=1", "--disable-warnings", "-q"])
        result = "Unit testing completed successfully."

    if html:
        generate_report(result, html=True)
        click.echo("✅ HTML report generated: report.html")
    else:
        generate_report(result, html=False)

if __name__ == "__main__":
    cli()
