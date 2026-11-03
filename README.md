
# Markdown Documentation Checker

## Overview

A lightweight Python utility that performs basic quality checks on Markdown documentation.

## Features

- Checks for missing H1 document titles.
- Identifies empty Markdown links.
- Detects trailing whitespace.
- Checks for required document sections.
- Generates a simple quality report.

## Technologies

- Python 3
- Regular Expressions
- pathlib
- Command-line arguments

## Installation

No external Python packages are required.

Ensure Python 3 is installed.

## Usage

Run the following command:

```bash
python markdown_checker.py installation-guide.md
```

## Sample Output

Documentation Quality Report: installation-guide.md

Found 1 issue(s):

- Missing required section: Conclusion

Check completed.

## Limitations

This is a basic rule-based checker. It does not verify whether technical instructions are factually correct or whether links actually work.

## Future Improvements

- Broken URL detection.
- Automated terminology checks.
- Style-guide compliance.
- GitHub Actions integration.

## Author

Diksha Gadhave
