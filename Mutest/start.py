"""
Interactive starter script for Mutest
Guides users through selecting tests and running mutation analysis
"""
import os
import sys
import json
from pathlib import Path
from mutest001 import MutantGenerator, MutationTestExecutor
from report import generate_text_report, generate_html_report, generate_json_report


# Test configurations: loaded from test_config.json
TEST_CONFIGS = {}


def load_saved_configs():
    """Load test configurations from JSON file"""
    config_file = 'test_config.json'
    global TEST_CONFIGS

    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                TEST_CONFIGS = json.load(f)
                print(f"✓ Loaded {len(TEST_CONFIGS)} test configurations from {config_file}")
        except Exception as e:
            print(f"Warning: Could not load configurations from {config_file}: {e}")
            print("Starting with empty configuration. Use option [2] to add tests.")
    else:
        print(f"Note: {config_file} not found. Starting with empty configuration.")
        print("Use option [2] from the main menu to add your first test.")


def print_header():
    """Print welcome header"""
    print("\n" + "=" * 70)
    print("  MUTEST - Interactive Mutation Testing")
    print("=" * 70)
    print()


def show_main_menu():
    """Display main menu"""
    print("=" * 70)
    print("  MAIN MENU")
    print("=" * 70)
    print(f"\n  Total Configured Tests: {len(TEST_CONFIGS)}")
    print()
    print("  [1] See all tests and run")
    print("  [2] Add new test")
    print("  [3] Remove test")
    print("  [q] Quit")
    print()
    print("=" * 70)


def show_available_tests():
    """Display all available tests with enhanced formatting"""
    print("\n" + "=" * 70)
    print("  ALL CONFIGURED TESTS")
    print("=" * 70)
    print(f"\n  Total Tests: {len(TEST_CONFIGS)}")
    print()

    if not TEST_CONFIGS:
        print("  No tests configured yet!")
        print("  Use option [2] from main menu to add a test.")
        print()
    else:
        for key, config in TEST_CONFIGS.items():
            print(f"  [{key}] {config['name']}")
            print(f"      Source: {config['source']}")
            print(f"      Tests:  {config['test_cmd']}")
            print()

    print("=" * 70)
    print("  RUN OPTIONS")
    print("=" * 70)
    print(f"  [all]   Run ALL tests")
    print(f"  [back]  Return to main menu")
    print()
    print("  Or enter a test number to run that specific test")
    print("=" * 70)


def get_main_menu_choice():
    """Get user choice from main menu"""
    while True:
        choice = input("\nSelect an option: ").strip().lower()

        if choice == 'q':
            print("\nExiting Mutest. Goodbye!")
            sys.exit(0)

        if choice in ['1', '2', '3']:
            return choice

        print(f"Invalid choice. Please enter 1, 2, 3, or q.")


def get_test_selection():
    """Prompt user to select a test from the tests menu"""
    while True:
        choice = input("\nSelect a test to run (number, 'all', or 'back'): ").strip().lower()

        if choice == 'back':
            return 'back'

        if choice == 'all':
            return 'all'

        if choice in TEST_CONFIGS:
            return choice

        print(f"Invalid choice '{choice}'. Please enter a valid test number, 'all', or 'back'.")


def add_new_test():
    """Interactive function to add a new test configuration"""
    print("\n" + "=" * 70)
    print("  ADD NEW TEST CONFIGURATION")
    print("=" * 70)
    print()

    # Get test name
    while True:
        test_name = input("Enter test name (e.g., 'My Function Tests'): ").strip()
        if test_name:
            break
        print("Test name cannot be empty. Please try again.")

    # Get source file path
    while True:
        source_file = input("Enter source file path (e.g., 'testing/simple_functions/my_file.py'): ").strip()
        if source_file:
            # Check if file exists
            if os.path.exists(source_file):
                break
            else:
                print(f"Warning: File '{source_file}' not found.")
                confirm = input("Continue anyway? (y/n): ").strip().lower()
                if confirm == 'y':
                    break
        else:
            print("Source file path cannot be empty. Please try again.")

    # Get test command
    while True:
        test_cmd = input("Enter test command (e.g., 'pytest tests/test_my_file.py -v'): ").strip()
        if test_cmd:
            break
        print("Test command cannot be empty. Please try again.")

    # Find next available key number
    existing_keys = [int(k) for k in TEST_CONFIGS.keys() if k.isdigit()]
    next_key = str(max(existing_keys) + 1) if existing_keys else "1"

    # Add to TEST_CONFIGS
    TEST_CONFIGS[next_key] = {
        "name": test_name,
        "source": source_file,
        "test_cmd": test_cmd
    }

    # Save to JSON file for persistence
    try:
        with open('test_config.json', 'w') as f:
            json.dump(TEST_CONFIGS, f, indent=4)
        print(f"\n✓ Test configuration saved to test_config.json!")
    except Exception as e:
        print(f"\nWarning: Could not save to file: {e}")
        print("Configuration added for this session only.")

    print()
    print("=" * 70)
    print(f"  NEW TEST ADDED: [{next_key}] {test_name}")
    print("=" * 70)
    print(f"  Source: {source_file}")
    print(f"  Tests:  {test_cmd}")
    print("=" * 70)
    print()

    return next_key


def remove_test():
    """Interactive function to remove a test configuration"""
    print("\n" + "=" * 70)
    print("  REMOVE TEST CONFIGURATION")
    print("=" * 70)
    print()

    if not TEST_CONFIGS:
        print("  No tests configured. Nothing to remove!")
        print()
        input("Press Enter to return to main menu...")
        return

    # Show all tests
    print("  Current Tests:")
    print()
    for key, config in TEST_CONFIGS.items():
        print(f"  [{key}] {config['name']}")
        print(f"      Source: {config['source']}")
        print()

    print("=" * 70)
    print()

    # Get test to remove
    while True:
        choice = input("Enter test number to remove (or 'back' to cancel): ").strip().lower()

        if choice == 'back':
            print("\nCancelled. Returning to main menu...")
            return

        if choice in TEST_CONFIGS:
            # Confirm deletion
            test_name = TEST_CONFIGS[choice]['name']
            confirm = input(f"\nAre you sure you want to remove '{test_name}'? (y/n): ").strip().lower()

            if confirm == 'y':
                removed_test = TEST_CONFIGS.pop(choice)

                # Save updated configs
                try:
                    with open('test_config.json', 'w') as f:
                        json.dump(TEST_CONFIGS, f, indent=4)
                    print(f"\n✓ Test '{test_name}' removed successfully!")
                except Exception as e:
                    print(f"\nWarning: Could not save changes: {e}")
                    print("Test removed for this session only.")

                print()
                input("Press Enter to return to main menu...")
                return
            else:
                print("\nCancelled. Test not removed.")
                return

        print(f"Invalid test number. Please try again.")


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

    if results['mutation_score'] >= 97:
        print("Status:           EXCELLENT test coverage!")
    elif results['mutation_score'] >= 90:
        print("Status:           GOOD test coverage - minor improvements possible")
    elif results['mutation_score'] >= 80:
        print("Status:           FAIR test coverage - some improvements needed")
    else:
        print("Status:           POOR test coverage - consider adding more tests")

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


def run_tests_menu():
    """Show tests and handle test running"""
    show_available_tests()

    if not TEST_CONFIGS:
        input("\nPress Enter to return to main menu...")
        return

    # Get test selection
    test_choice = get_test_selection()

    # Handle back to main menu
    if test_choice == 'back':
        return

    # Get report format
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
    input("Press Enter to return to main menu...")


def main():
    """Main function with menu loop"""
    while True:
        print_header()
        show_main_menu()

        choice = get_main_menu_choice()

        if choice == '1':
            # See all tests and run
            run_tests_menu()

        elif choice == '2':
            # Add new test
            new_test_key = add_new_test()

            # Ask if user wants to run the new test now
            run_now = input("Would you like to run this test now? (y/n): ").strip().lower()
            if run_now == 'y':
                # Get report format
                report_format = get_report_format()

                print("\n" + "=" * 70)
                print("Starting Mutation Testing...")
                print("=" * 70)

                # Run the new test
                config = TEST_CONFIGS[new_test_key]
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
                input("\nPress Enter to return to main menu...")
            else:
                print("\nTest saved. Returning to main menu...")
                input("Press Enter to continue...")

        elif choice == '3':
            # Remove test
            remove_test()


if __name__ == "__main__":
    try:
        # Load saved configurations on startup
        load_saved_configs()
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
