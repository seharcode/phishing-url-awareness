# Test Results

Python version used: Python 3.11+ recommended (record your exact local version after running)
Operating system: Record your operating system
Date: Record the date you run the tests

> The expected observations below follow the workbook. Run each sample locally and update the
> Actual and Pass/Fail columns honestly before submitting. Automated tests are also available in
> `test_phishing_checker.py`.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; not a safety guarantee | Fill after running locally | Pending |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Fill after running locally | Pending |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Fill after running locally | Pending |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Fill after running locally | Pending |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Fill after running locally | Pending |

## Notes

- Update the actual results and pass/fail status after running the program on your computer.
- The tool checks selected text patterns only. A URL with no listed signs may still be dangerous.
