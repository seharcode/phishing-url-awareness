"""Automated tests for the Phishing URL Awareness Checker."""
import unittest
from phishing_checker import inspect_url, has_warnings


class InspectUrlTests(unittest.TestCase):
    def test_https_example_has_no_listed_signs(self):
        self.assertEqual(
            inspect_url("https://www.example.com/login"),
            ["No listed warning signs found. This does NOT prove safety."],
        )

    def test_documentation_ip_and_http(self):
        result = inspect_url("http://192.0.2.10/account")
        self.assertIn("Uses an IP address instead of a familiar domain.", result)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", result)

    def test_at_symbol_and_http(self):
        result = inspect_url("http://example.com@sample.invalid/login")
        self.assertIn("Contains an @ symbol; inspect carefully.", result)
        self.assertIn("Uses HTTP. HTTPS alone does not prove trust.", result)

    def test_many_hostname_labels(self):
        self.assertIn(
            "Contains many hostname segments/subdomains.",
            inspect_url("https://a.b.c.d.e.example.invalid/path"),
        )

    def test_punycode_marker(self):
        self.assertIn(
            "Contains a punycode-style hostname.",
            inspect_url("https://xn--example.invalid/"),
        )

    def test_long_url(self):
        url = "https://www.example.com/" + ("a" * 90)
        self.assertIn(
            "Unusually long URL (over 100 characters).",
            inspect_url(url),
        )

    def test_empty_input(self):
        self.assertEqual(inspect_url("   "), ["No URL entered."])

    def test_malformed_url_does_not_crash(self):
        self.assertEqual(
            inspect_url("http://[bad"),
            ["This text is not a valid URL format."],
        )

    def test_missing_scheme_is_treated_as_http(self):
        self.assertIn(
            "Uses HTTP. HTTPS alone does not prove trust.",
            inspect_url("www.example.com"),
        )

    def test_no_warning_message_is_not_a_warning(self):
        self.assertFalse(has_warnings(inspect_url("https://www.example.com/login")))

    def test_warning_summary_detects_warning(self):
        self.assertTrue(has_warnings(inspect_url("http://192.0.2.10/account")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
