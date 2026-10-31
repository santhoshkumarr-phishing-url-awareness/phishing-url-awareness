
"""EWB Phishing URL Awareness Checker."""

from urllib.parse import urlsplit
import ipaddress

MAX_URL_LENGTH = 100
MAX_HOST_LABELS = 4


def check_url(url):
    warnings = []
    candidate = url.strip()

    if "@" in candidate:
        warnings.append("Contains an @ symbol (may hide the real destination).")

    if len(candidate) > MAX_URL_LENGTH:
        warnings.append(f"Unusually long URL ({len(candidate)} characters).")

    parse_target = candidate if "://" in candidate else "//" + candidate

    try:
        parsed = urlsplit(parse_target)
        hostname = parsed.hostname or ""
    except ValueError:
        warnings.append("Malformed URL: hostname could not be parsed.")
        return warnings

    if not hostname:
        warnings.append("Malformed URL: no hostname was found.")
        return warnings

    try:
        ipaddress.ip_address(hostname)
        warnings.append("Uses an IP address instead of a familiar domain.")
    except ValueError:
        pass

    labels = hostname.split(".")

    if len(labels) > MAX_HOST_LABELS:
        warnings.append("Has many hostname segments.")

    if any(label.lower().startswith("xn--") for label in labels):
        warnings.append("Contains a punycode hostname marker (xn--).")

    scheme = parsed.scheme.lower() if "://" in candidate else ""

    if scheme == "http":
        warnings.append("Uses HTTP. HTTPS alone does not prove trust.")

    return warnings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")
    print("-" * 55)

    while True:
        url = input("\nEnter a URL to check (or q to quit): ").strip()

        if url.lower() in ["q", "quit", "exit"]:
            print("Thank you for using EWB URL Checker.")
            break

        if not url:
            print("Input cannot be empty. Please try again.")
            continue

        findings = check_url(url)

        if findings:
            print("\nWarning signs found:")

            for number, finding in enumerate(findings, start=1):
                print(f"{number}. {finding}")

            print("\nREVIEW CAREFULLY!")
            print("One or more warning signs were detected.")
        else:
            print("\nNo listed warning signs found. This does NOT prove safety.")
            

        print("\nCaution:")
        print("This tool only checks URL text.")
        print("It does not open websites or scan for malware.")
        print("It does not check URL reputation.")


if __name__ == "__main__":
    main()
