"""
Interactive starter script for Mutest
Guides users through selecting tests and running mutation analysis
"""
import os
import sys
from pathlib import Path
from mutest001 import MutantGenerator, MutationTestExecutor
from report import generate_text_report, generate_html_report, generate_json_report


# Test configurations: maps source files to their test commands
TEST_CONFIGS = {
    "1": {
        "name": "Math Utils",
        "source": "testing/simple_functions/math_utils.py",
        "test_cmd": "pytest testing/unit_test/test_001.py -v"
    },
    "2": {
        "name": "Calculator",
        "source": "testing/simple_functions/calculator.py",
        "test_cmd": "pytest testing/advanced_tests/test_good_coverage.py -v"
    },
    "3": {
        "name": "Temperature Converter",
        "source": "testing/simple_functions/temperature.py",
        "test_cmd": "pytest testing/advanced_tests/test_good_coverage.py -v"
    },
    "4": {
        "name": "String Utils",
        "source": "testing/simple_functions/string_utils.py",
        "test_cmd": "pytest testing/unit_test/test_001.py -v"
    },
    "5": {
        "name": "Grade Utils",
        "source": "testing/simple_functions/grade_utils.py",
        "test_cmd": "pytest testing/unit_test/test_001.py -v"
    },
    "6": {
        "name": "Loop Functions",
        "source": "testing/simple_functions/loop_functions.py",
        "test_cmd": "pytest testing/advanced_tests/test_timeout_loops.py -v"
    },
    "7": {
        "name": "Recursive Functions",
        "source": "testing/simple_functions/recursive_functions.py",
        "test_cmd": "pytest testing/advanced_tests/test_timeout.py -v"
    }
}


def print_header():
    """Print welcome header"""
    print("\n" + "=" * 70)
    print("  MUTEST - Interactive Mutation Testing")
    print("=" * 70)
    print()


def show_available_tests():
    """Display all available tests"""
    print("Available Tests:")
    print("-" * 70)
    for key, config in TEST_CONFIGS.items():
        print(f"  [{key}] {config['name']}")
        print(f"      Source: {config['source']}")
        print(f"      Tests:  {config['test_cmd']}")
        print()
    print(f"  [all] Run ALL tests")
    print(f"  [q] Quit")
    print("-" * 70)


def get_test_selection():
    """Prompt user to select a test"""
    while True:
        choice = input("\nSelect a test to run (enter number, 'all', or 'q'): ").strip().lower()

        if choice == 'q':
            print("\nExiting Mutest. Goodbye!")
            sys.exit(0)

        if choice == 'all':
            return 'all'

        if choice in TEST_CONFIGS:
            return choice

        print(f"Invalid choice '{choice}'. Please enter a valid number, 'all', or 'q'.")


def get_report_format():
    """Prompt user to select report format"""
    print("\nReport Format Options:")
    print("  [1] HTML  - Interactive web-based report (recommended)")
    print("  [2] Text  - Plain text report")
    print("  [3] JSON  - Machine-readable JSON")
    print("  [4] All   - Generate all formats")

    formats = {
        '1': 'html',
        '2': 'text',
        '3': 'json',
        '4': 'all'
    }

    while True:
        choice = input("\nSelect report format (1-4): ").strip()

        if choice in formats:
            return formats[choice]

        print(f"Invalid choice. Please enter 1, 2, 3, or 4.")


def run_mutation_test(source_file, test_command, test_name):
    """Run mutation test for a single configuration"""
    print("\n" + "=" * 70)
    print(f"Testing: {test_name}")
    print("=" * 70)
    print(f"Source: {source_file}")
    print(f"Tests:  {test_command}")
    print()

    # Read source code
    try:
        with open(source_file, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"ERROR: Could not find source file: {source_file}")
        return None
    except Exception as e:
        print(f"ERROR: Failed to read file: {e}")
        return None

    # Generate mutants
    print("Generating mutants...")
    generator = MutantGenerator()
    mutants = generator.generate_mutants(source_code)
    print(f"Generated {len(mutants)} mutants")

    if len(mutants) == 0:
        print("No mutations found. The source file may not have mutable operators.")
        return None

    # Run mutation tests
    print(f"\nRunning tests against {len(mutants)} mutants...")
    print("-" * 70)
    executor = MutationTestExecutor(source_file, test_command)
    results = executor.run_mutation_tests(mutants)

    if not results:
        print("ERROR: Mutation testing failed!")
        return None

    # Display summary
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"Total Mutants:    {results['total']}")
    print(f"Killed:           {results['killed_count']} (GOOD - tests caught these)")
    print(f"Survived:         {results['survived_count']} (BAD - tests missed these)")
    print(f"Timeout:          {results['timeout_count']}")
    print(f"\nMutation Score:   {results['mutation_score']:.2f}%")

    if results['mutation_score'] >= 80:
        print("Status:           EXCELLENT test coverage!")
    elif results['mutation_score'] >= 60:
        print("Status:           GOOD test coverage")
    else:
        print("Status:           WEAK test coverage - consider adding more tests")

    print("=" * 70)

    return results


def generate_reports(results, report_format, source_file, test_command, test_name):
    """Generate reports in the selected format(s)"""
    if not results:
        return

    # Create reports directory
    reports_dir = Path('reports')
    reports_dir.mkdir(exist_ok=True)

    # Generate safe filename from test name
    safe_name = test_name.lower().replace(' ', '_')

    print("\nGenerating reports...")

    if report_format in ['html', 'all']:
        output_file = f'reports/{safe_name}_report.html'
        generate_html_report(results, output_file, source_file, test_command)
        print(f"  ✓ HTML report: {output_file}")

    if report_format in ['text', 'all']:
        output_file = f'reports/{safe_name}_report.txt'
        generate_text_report(results, output_file, source_file, test_command)
        print(f"  ✓ Text report: {output_file}")

    if report_format in ['json', 'all']:
        output_file = f'reports/{safe_name}_report.json'
        generate_json_report(results, output_file, source_file, test_command)
        print(f"  ✓ JSON report: {output_file}")


def main():
    """Main interactive function"""
    print_header()
    show_available_tests()

    # Get user selections
    test_choice = get_test_selection()
    report_format = get_report_format()

    print("\n" + "=" * 70)
    print("Starting Mutation Testing...")
    print("=" * 70)

    # Run selected test(s)
    if test_choice == 'all':
        print(f"\nRunning ALL {len(TEST_CONFIGS)} tests...\n")
        all_results = []

        for key, config in TEST_CONFIGS.items():
            results = run_mutation_test(
                config['source'],
                config['test_cmd'],
                config['name']
            )

            if results:
                all_results.append({
                    'name': config['name'],
                    'results': results,
                    'source': config['source'],
                    'test_cmd': config['test_cmd']
                })
                generate_reports(
                    results,
                    report_format,
                    config['source'],
                    config['test_cmd'],
                    config['name']
                )

            print("\n")

        # Print overall summary
        print("\n" + "=" * 70)
        print("OVERALL SUMMARY - ALL TESTS")
        print("=" * 70)
        for item in all_results:
            score = item['results']['mutation_score']
            status = "✓" if score >= 80 else "⚠" if score >= 60 else "✗"
            print(f"{status} {item['name']:30} Score: {score:6.2f}%")
        print("=" * 70)

    else:
        # Run single test
        config = TEST_CONFIGS[test_choice]
        results = run_mutation_test(
            config['source'],
            config['test_cmd'],
            config['name']
        )

        if results:
            generate_reports(
                results,
                report_format,
                config['source'],
                config['test_cmd'],
                config['name']
            )

    print("\nMutation testing complete!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
