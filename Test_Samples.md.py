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