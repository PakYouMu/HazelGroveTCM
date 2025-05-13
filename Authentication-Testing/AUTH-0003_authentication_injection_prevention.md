## **AUTH-0003:** Authentication - Injection Prevention

> **Summary:** Ensure the system protects against common web vulnerabilities by sanitizing or rejecting inputs containing malicious scripts or injection patterns in authentication forms. <br>

**Preconditions:**

- The user is interacting with the sign-up, sign-in, or forgot password forms.
- The application's authentication services are operational.

**Test Steps:**

| \# | Step Description                                                                                          | Expected Result                                                                                                                              |
|----|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A user attempts to sign up by entering a malicious script (e.g., `<script>alert('xss')</script>`) into the email field. | The system either rejects the input displaying an error like "Invalid input" or "Invalid email address," and prevents account creation without executing the script. |
| 2  | A user attempts to sign up by entering a malicious script into the password field.                             | The system rejects the input, displaying an error like "Invalid input," and prevents account creation without processing the script.        |
| 3  | A user attempts to sign in by entering a malicious script into the email field.                               | The system either rejects the input displaying an error like "Invalid input" or "Invalid email address," and prevents the sign-in attempt without executing the script. |
| 4  | A user attempts to sign in by entering a valid email and a malicious script into the password field.           | The system rejects the input, displaying an error like "Invalid input," and prevents the sign-in attempt without processing the script.    |
| 5  | A user attempts to request a password reset by entering a malicious script into the email field on the forgot password page. | The system either rejects the input displaying an error like "Invalid input" or "Invalid email address," and does not send a reset link. |

**Post-conditions:**

- The malicious script is not executed or stored.
- The application's integrity and user data remain secure.
- The user is prevented from proceeding with the malicious input and may be shown an error message.
