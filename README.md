# EWB Phishing URL Awareness Checker

A beginner-friendly Python command-line project that checks URL text for six visible warning signs associated with phishing. It is designed for defensive learning and does **not** visit URLs, make network requests, scan websites, or prove whether a URL is safe.

## Features

- Detects an `@` symbol in the URL text.
- Flags URLs longer than 100 characters.
- Flags IPv4-shaped hostnames.
- Flags hostnames with five or more dot-separated labels.
- Flags punycode-style hostnames containing `xn--`.
- Flags the HTTP scheme.
- Explains why each warning may matter.
- Repeats checks until the user types `q`, `quit`, or `exit`.
- Handles blank and malformed input without crashing.
- Includes automated unit tests and a workbook-aligned manual test table.

## Requirements

- Python 3.10 or later.
- VS Code is recommended.
- No third-party packages and no API keys are required.

## Project structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── .gitignore
├── tests/
│   ├── test_phishing_checker.py
│   └── test_samples.md
└── screenshots/
    ├── README.md
    ├── sample_run.png
    └── test_results.png
```

The PNG files currently are labelled example previews, not screenshots from your own computer. Replace them with genuine screenshots of your local run before submission, as required by the workbook.

## Setup in VS Code

1. Install Python 3.10+ from [python.org](https://www.python.org/downloads/).
   - Windows: enable **Add python.exe to PATH** during installation.
2. Install [VS Code](https://code.visualstudio.com/) and the Microsoft Python extension.
3. In VS Code, choose **File → Open Folder** and select `phishing-url-awareness`.
4. Open **Terminal → New Terminal**.
5. Check Python:
   - Windows: `python --version` or `py --version`
   - macOS/Linux: `python3 --version`

## Run the checker

In the VS Code terminal, from the project folder:

**Windows**
```powershell
python phishing_checker.py
```

If needed, use:
```powershell
py phishing_checker.py
```

**macOS/Linux**
```bash
python3 phishing_checker.py
```

Try only the workbook's reserved example strings, such as:

```text
http://192.0.2.10/account
https://www.example.com/login
http://example.com@sample.invalid/login
https://a.b.c.d.e.example.invalid/path
https://xn--example.invalid/
```

Type `q` to exit.

## Example output

```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.
Use the workbook's sample strings for practice.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
  Why it matters: A numeric host can make it harder to recognise which service you are contacting.
- Uses HTTP. HTTPS alone does not prove trust.
  Why it matters: HTTP does not encrypt the connection. HTTPS is useful, but it does not prove a site is honest.

REVIEW CAREFULLY: 2 warning sign(s) found.

Never enter passwords from unexpected links.
```

## Run automated tests

No installation step is needed because the tests use Python's built-in `unittest` module.

**Windows**
```powershell
python -m unittest discover -s tests -v
```

**macOS/Linux**
```bash
python3 -m unittest discover -s tests -v
```

The tests cover the workbook's five sample patterns, long URLs, blank input, malformed input, missing schemes, and warning-summary logic.

## Manual testing evidence

Open `tests/test_samples.md`. Run the five workbook sample strings and fill in the actual results and PASS/FAIL values. Do not claim a test passed unless you ran it and observed the expected behaviour.

## Screenshots

- `screenshots/sample_run.png`
- `screenshots/test_results.png`

These are clearly marked example previews included to show the intended framing. Replace both with genuine screenshots from your own VS Code terminal and test file before submitting:
- `sample_run.png`: show the command, sample input, and printed findings.
- `test_results.png`: show your completed manual test table or the automated test output.

## Improvements included

1. **Repeat-and-quit menu:** inspect multiple sample strings without restarting the program.
2. **Malformed-input handling:** catches parsing errors such as `http://[bad` and returns a message instead of crashing.
3. **Warning explanations and summary:** provides a short reason for each warning and displays a `REVIEW CAREFULLY` summary when warning signs are present.

## Limitations

These checks are simple clues, not a security verdict. Some legitimate URLs may trigger warnings, and harmful URLs may trigger none. The IP pattern check follows the workbook's simple IPv4-shaped text pattern and is not a full IP validation routine. HTTPS does not guarantee that a website is honest.

## Ethical use

- Use the reserved sample strings in the workbook for practice.
- Do not open suspicious links to test them.
- Do not probe or scan websites or networks without written authorisation.
- Do not collect credentials or upload passwords, tokens, or private data.
- Describe this as a learning tool, not a production phishing-detection service.

## Author

Update this section with your own name, batch/course, and any details requested by your coordinator.
