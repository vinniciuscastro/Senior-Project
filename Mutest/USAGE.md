# Mutest - Usage Guide

## Quick Start

Run the interactive starter:
```bash
python start.py
```

---

## Main Menu

When you run `start.py`, you'll see the main menu with three options:

```
======================================================================
  MAIN MENU
======================================================================

  Total Configured Tests: 7

  [1] See all tests and run
  [2] Add new test
  [3] Remove test
  [q] Quit
```

### Menu Options

**[1] See all tests and run**
- View all configured test cases
- Run individual tests or all tests
- Returns to main menu when done

**[2] Add new test**
- Interactively add a new test configuration
- Option to run the new test immediately
- Automatically saved for future use

**[3] Remove test**
- View all tests
- Select a test to remove
- Confirmation required before deletion

**[q] Quit**
- Exit the program

---

## Option 1: See All Tests and Run

### What You'll See

After selecting option [1], you'll see all configured tests:

```
======================================================================
  ALL CONFIGURED TESTS
======================================================================

  Total Tests: 7

  [1] Math Utils
      Source: testing/simple_functions/math_utils.py
      Tests:  pytest testing/unit_test/test_001.py -v

  [2] Calculator
      Source: testing/simple_functions/calculator.py
      Tests:  pytest testing/advanced_tests/test_good_coverage.py -v

  ... (more tests)

======================================================================
  RUN OPTIONS
======================================================================
  [all]   Run ALL tests
  [back]  Return to main menu

  Or enter a test number to run that specific test
======================================================================
```

### Running Tests

- **Enter a number** (e.g., `1`) - Run that specific test
- **Type `all`** - Run all tests sequentially
- **Type `back`** - Return to main menu without running tests

After running tests, you'll be returned to the main menu.

---

## Option 2: Adding a New Test Configuration

1. **Select 'new' from the main menu**

2. **Enter test details:**
   - **Test Name**: A descriptive name (e.g., "My Function Tests")
   - **Source File Path**: Path to the Python file to mutate (e.g., "testing/simple_functions/my_file.py")
   - **Test Command**: Command to run your tests (e.g., "pytest tests/test_my_file.py -v")

3. **File validation:**
   - If the source file doesn't exist, you'll get a warning
   - You can choose to continue anyway

4. **Auto-save:**
   - Your configuration is automatically saved to `test_configs.json`
   - It will be available in future sessions

5. **Run immediately (optional):**
   - You'll be asked if you want to run the test right away
   - Choose 'y' to run it now, or 'n' to save for later

---

---

## Option 3: Remove a Test Configuration

### How to Remove Tests

1. **Select option [3] from main menu**

2. **View all tests:**
   ```
   ======================================================================
     REMOVE TEST CONFIGURATION
   ======================================================================

     Current Tests:

     [1] Math Utils
         Source: testing/simple_functions/math_utils.py

     [2] Calculator
         Source: testing/simple_functions/calculator.py

     ... (more tests)
   ```

3. **Enter test number to remove** or type `back` to cancel

4. **Confirm deletion:**
   ```
   Are you sure you want to remove 'Calculator'? (y/n):
   ```

5. **Test is removed and changes are saved**

**Note:** Default tests (1-7) can be removed, but they won't be deleted from the original code—only from your active configuration.

---

## Example Workflows

### Example 1: Adding a New Test

```
Select an option: new

  ADD NEW TEST CONFIGURATION
======================================================================

Enter test name: My Custom Module
Enter source file path: testing/simple_functions/custom_module.py
Enter test command: pytest testing/unit_test/test_custom.py -v

✓ Test configuration saved!

======================================================================
  NEW TEST ADDED: [8] My Custom Module
======================================================================
  Source: testing/simple_functions/custom_module.py
  Tests:  pytest testing/unit_test/test_custom.py -v
======================================================================

Would you like to run this test now? (y/n): n

Test saved. Returning to main menu...
Press Enter to continue...
```

### Example 2: Running a Specific Test

```
# From main menu, select option 1
Select an option: 1

# See all tests, then select one
Select a test to run: 2

# Choose report format
Select report format (1-4): 1

# Test runs and generates HTML report
# After completion, press Enter to return to main menu
```

### Example 3: Running All Tests

```
# From main menu, select option 1
Select an option: 1

# Select 'all' to run everything
Select a test to run: all

# Choose report format
Select report format (1-4): 1

# All tests run sequentially with summary at the end
```

### Example 4: Removing a Test

```
# From main menu, select option 3
Select an option: 3

# See list of tests and select one
Enter test number to remove: 8

# Confirm deletion
Are you sure you want to remove 'My Custom Module'? (y/n): y

✓ Test 'My Custom Module' removed successfully!

Press Enter to return to main menu...
```

---

## Persistent Configurations

- All test configurations are saved to `test_configs.json`
- When you run `start.py` again, your saved tests are automatically loaded
- Default tests (1-7) are always available
- Your custom tests get assigned numbers starting from 8

---

## Report Formats

After selecting a test, choose your report format:

1. **HTML** - Interactive web-based report (recommended)
2. **Text** - Plain text report
3. **JSON** - Machine-readable JSON format
4. **All** - Generate all three formats

Reports are saved to the `reports/` directory.

---

## Tips

- **Test Command Format**: Make sure your test command works from the Mutest directory
- **Relative Paths**: Use relative paths from the Mutest directory
- **File Check**: The program will warn you if the source file doesn't exist
- **Running All Tests**: Use 'all' to run every configured test and get an overall summary
- **Backup**: The `test_configs.json` file contains all your custom tests - keep it safe!

---

## Troubleshooting

**"File not found" error:**
- Make sure the path is relative to the Mutest directory
- Check for typos in the filename

**Test command fails:**
- Verify the test command works when run manually
- Check that pytest is installed
- Ensure test file paths are correct

**Configuration not saved:**
- Check file permissions in the Mutest directory
- Look for error messages during save

---

## File Structure

```
Mutest/
├── start.py              # Interactive launcher (enhanced!)
├── test_configs.json     # Saved test configurations (auto-created)
├── mutest001.py          # Core mutation testing engine
├── report.py             # Report generation
├── reports/              # Generated reports directory
└── testing/              # Your test files and source code
```

---

## Advanced Usage

### Editing Configurations

To edit or delete a test configuration:
1. Open `test_configs.json` in a text editor
2. Modify or remove entries as needed
3. Save the file
4. Run `python start.py` to see changes

### Backing Up Configurations

```bash
# Backup your custom tests
cp test_configs.json test_configs.backup.json
```

---

## What's New

✨ **Enhanced Start Menu**
- Better visual layout
- Shows total test count
- Clear separation of tests and options

✨ **Add New Tests**
- Interactive test configuration
- File validation
- Auto-save to JSON
- Run immediately or save for later

✨ **Persistent Storage**
- Configurations saved across sessions
- Auto-load on startup
- Easy backup and sharing

---

Happy Testing! 🧬
