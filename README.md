# EWB Phishing URL Awareness Checker

## Overview

Phishing is a cyberattack in which attackers use deceptive links or websites to trick people into sharing sensitive information such as passwords, banking details, and personal data. This Python application checks URL text for six common warning signs that may indicate a suspicious link. It helps users become more aware of potentially risky URLs without opening or visiting any website.

## Features

- Detects an `@` symbol in the URL.
- Flags unusually long URLs (over 100 characters).
- Flags IP-address hostnames.
- Flags many hostname segments (5 or more).
- Flags punycode-style hostnames (`xn--`).
- Flags the HTTP scheme instead of HTTPS.
- Allows users to check multiple URLs without restarting the program.
- Displays a clear "REVIEW CAREFULLY" message when warning signs are detected.
- Handles malformed URLs and missing hostnames with clear error messages.

## Requirements

- Python 3.10 or later.
- No additional Python packages required.
- Uses Python standard libraries.

## How to Run

**Windows:**

```bash
python url_checker.py
```

**Mac/Linux:**

```bash
python3 url_checker.py
```

The application asks the user to enter a URL as text. Type `q` to quit.

## Example Output

```text
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.
-------------------------------------------------------

Enter a URL to check: http://192.0.2.10/login

Warning signs found:
1. Uses an IP-address hostname instead of a domain name.
2. Uses HTTP instead of encrypted HTTPS.

REVIEW CAREFULLY!
One or more warning signs were detected.

Caution:
This tool only checks URL text.
It does not open websites or scan for malware.
It does not check URL reputation.
```

# Test Results
Python version used: 3.12.10                      | Operating system: Windows11                                                               | Date: 31/10/2026
| # | Input                                       | Expected result            | Actual result                                                | Pass/Fail |
|---|---------------------------------------------|----------------------------|--------------------------------------------------------------|-----------|
| 1 | https://www.example.com/login               | No listed warning signs    | No listed warning signs found. This does NOT prove safety.   |    pass   |

| 2 | http://192.0.2.10/account                   | IP address + HTTP          | Uses an IP address instead of a familiar domain.             |    pass   |
									       | Uses HTTP. HTTPS alone does not prove trust..                
    
| 3 | http://example.com@sample.invalid/login     | @ symbol + HTTP            | Contains an @ symbol; inspect carefully.                     |    pass   |
                                                                                 Uses HTTP. HTTPS alone does not prove trust.

| 4 | https://a.b.c.d.e.example.invalid/path      | Many hostname segments     | Contains many hostname segments/subdomains (7 labels).       |    pass   |

| 5 | https://xn--example.invalid/                | Punycode-style hostname    | Contains a punycode-style hostname.                          |    pass   |


# Bonus Check

| # | Input                                       | Expected result            | Actual result                                              | Pass/Fail |
|---|---------------------------------------------|----------------------------|------------------------------------------------------------|-----------|
| 1 | (just press Enter)                          | Empty URL                  | No URL Entered                                             |    pass   |
| 2 | www.example.com                             | http:// missing            | No listed warning signs found. This does NOT prove safety. |    pass   |
| 3 | https://secure-login.example.invalid        | No sign found              | No listed warning signs found. This does NOT prove safety. |    pass   |
| 3 | http://[bad                                 | The Program stops          | ValueError: Invalid IPv6 URL                               |    pass   |

## Notes
Through this project, I learned how to use Python URL parsing, string operations and conditional statements to identify six common URL warning signs. 
I also learned how to write test cases and document a cybersecurity application.

What surprised me was that even a URL with HTTPS and no warning signs could still be malicious. 
I understood that detecting warning signs does not guarantee that a website is safe.

## Screenshots

(G:\Future Plan\Intershi or Job\Intership Applied\AI POWERED CYBERSECURITY\Final Project\url_warning_checker_submission\screenshots/sample_run.png)
(G:\Future Plan\Intershi or Job\Intership Applied\AI POWERED CYBERSECURITY\Final Project\url_warning_checker_submission\screenshots/test_result1.png/test_result2.png/test_result3.png)

## Improvements

### 1. Multiple URL Checking (Option A – Easy)

**What changed:** Added a continuous loop using Python's `while` statement.

**Why:** Users can check multiple URLs without restarting the application.

**How tested:** Entered multiple URLs consecutively and used `q` to exit the application.

### 2. Review Carefully Summary (Option B – Easy)

**What changed:** Added a clear "REVIEW CAREFULLY" message whenever one or more warning signs are detected.

**Why:** Helps users understand that the URL requires further attention.

**How tested:** Entered HTTP and IP-address URLs and verified that the warning summary appeared.

### 3. Malformed Input Handling (Option C – Medium)

**What changed:** Added exception handling using `try` and `except` to handle malformed URL input and missing hostnames.

**Why:** Prevents unexpected parsing errors from terminating the program.

**How tested:** Entered incorrectly formatted URLs and verified that the application displayed an understandable error message.

## Limitations

This is an educational cybersecurity awareness tool. It only reads URL text.

- It does not visit or open URLs.
- It does not scan for malware.
- It does not contact external URL reputation services.
- It does not prove that a URL is safe.

**No warning signs found does NOT mean a URL is safe.**

A malicious URL may have none of the six warning signs checked by this application.

## Ethical Use

- Use sample URL strings for testing.
- Do not collect passwords or credentials.
- Do not use this project to deceive anyone.
- Do not test websites or systems without permission.
- Use this application only for educational and defensive cybersecurity awareness.

## Author

Santhosh Kumar R  
EWB Courses – Cybersecurity Mini Project  
Project: Phishing URL Awareness Checker