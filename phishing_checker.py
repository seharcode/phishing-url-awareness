"""EWB Phishing URL Awareness Checker.

Defensive learning tool: inspects URL text only. It never opens URLs,
makes network requests, or declares a URL safe or malicious.
"""
import re
from urllib.parse import urlparse

# Keep these messages stable so test evidence and documentation stay consistent.
INFO_PREFIXES = (
    "No URL entered.",
    "Could not identify a hostname.",
    "This text is not a valid URL format.",
    "No listed warning signs found.",
)

WARNING_REASONS = {
    "Contains an @ symbol; inspect carefully.":
        "Text before @ can be misleading; the hostname after it may be the destination.",
    "Unusually long URL (over 100 characters).":
        "Long links can make the destination harder to notice, although legitimate links can also be long.",
    "Uses an IP address instead of a familiar domain.":
        "A numeric host can make it harder to recognise which service you are contacting.",
    "Contains many hostname segments/subdomains.":
        "Several hostname labels can make a link look more official than it is.",
    "Contains a punycode-style hostname.":
        "Punycode can represent international characters, including characters that resemble other letters.",
    "Uses HTTP. HTTPS alone does not prove trust.":
        "HTTP does not encrypt the connection. HTTPS is useful, but it does not prove a site is honest.",
}


def inspect_url(raw_url):
    """Return a list of findings for the supplied URL text."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # This follows the workbook's visible-pattern check. It is a clue, not
    # a full IP-address validator.
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")

    return findings


def has_warnings(findings):
    """Return True when findings contain warning signs rather than information."""
    if not findings:
        return False
    return not findings[0].startswith(INFO_PREFIXES)


def print_result(raw_url):
    """Print findings, short explanations, and a cautious summary."""
    findings = inspect_url(raw_url)
    print("\nResult:")
    for item in findings:
        print("- " + item)
        reason = WARNING_REASONS.get(item)
        if reason:
            print("  Why it matters: " + reason)

    if has_warnings(findings):
        print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
    elif findings[0].startswith("No listed warning signs"):
        print("\nNo listed warning signs were detected. This is NOT a safety guarantee.")
    else:
        print("\nPlease enter a URL as text and try again.")


def main():
    """Run the interactive checker until the user enters q, quit, or exit."""
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("Use the workbook's sample strings for practice.")

    while True:
        try:
            raw_url = input("\nEnter a sample URL (or type q to quit): ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! Stay alert online.")
            break

        if raw_url.strip().lower() in {"q", "quit", "exit"}:
            print("Goodbye! Stay alert online.")
            break

        print_result(raw_url)
        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
