
import re
import sys
from pathlib import Path

def check_markdown(file_path):
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        print("Error: File not found.")
        return

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    issues = []

    # Check for a document title
    if not re.search(r"^#\s+\S+", content, re.MULTILINE):
        issues.append("Missing document title (H1 heading).")

    # Check for empty Markdown links
    for number, line in enumerate(lines, start=1):
        if re.search(r"\[[^\]]+\]\(\s*\)", line):
            issues.append(f"Line {number}: Empty Markdown link.")

        # Check trailing whitespace
        if line.rstrip() != line:
            issues.append(f"Line {number}: Trailing whitespace.")

    # Check required sections
    required_sections = ["Overview", "Conclusion"]

    for section in required_sections:
        pattern = rf"^##\s+{re.escape(section)}\s*$"

        if not re.search(pattern, content, re.MULTILINE):
            issues.append(f"Missing required section: {section}")

    # Display report
    print(f"\nDocumentation Quality Report: {path.name}")
    print("-" * 45)

    if issues:
        print(f"Found {len(issues)} issue(s):\n")

        for issue in issues:
            print("- " + issue)
    else:
        print("No issues found!")

    print("\nCheck completed.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python markdown_checker.py <file.md>")
    else:
        check_markdown(sys.argv[1])
