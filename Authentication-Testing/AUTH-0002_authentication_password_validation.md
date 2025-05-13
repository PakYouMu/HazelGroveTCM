## **AUTH-0002:** Authentication - Password Validation

> **Summary:** Ensure the system enforces the minimum password length requirement when a new user creates an account. <br>

**Preconditions:**

- The user is on the sign-up page of the application.
- The application's authentication services are operational.

**Test Steps:**

| \# | Step Description                                                                           | Expected Result                                                                                                |
|----|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 1  | A new user attempts to sign up by entering a password that is shorter than the required 8 characters, along with other valid sign-up details (e.g., valid email, username). | The system displays an error message on the sign-up page, such as "Password must be at least 8 characters long," and does not create the account. |

**Post-conditions:**

- The user's account is not created.
- The user remains on the sign-up page with an opportunity to correct their password.