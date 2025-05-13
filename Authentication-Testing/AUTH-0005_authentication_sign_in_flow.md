## **AUTH-0005:** Authentication - Sign In Flow

> **Summary:** Verify that a registered user can successfully sign in with correct credentials, and the system appropriately handles incorrect credentials or attempts to sign in with non-existent accounts. <br>

**Preconditions:**

- The user is on the sign-in page.
- The application's authentication services are operational.
- For positive tests, a user account with known credentials exists.

**Test Steps:**

| \# | Step Description                                                                                                | Expected Result                                                                                                                                           |
|----|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A registered user enters their correct email address and password and submits the sign-in form.                    | The system authenticates the user successfully. The user is granted access and redirected to their dashboard or the main application area (e.g., `/protected`). |
| 2  | A user attempts to sign in using an email address that is not registered in the system.                            | The system displays an error message on the sign-in page, such as "Email not found" or "No account found with this email."                                    |
| 3  | A registered user enters their correct email address but an incorrect password and submits the sign-in form.         | The system displays an error message on the sign-in page, such as "Incorrect password" or "Invalid credentials." The user is not logged in.                 |
| 4  | A user attempts to sign in without entering an email address or a password, or both.                              | The system displays an error message on the sign-in page, such as "Email and password are required."                                                      |

**Post-conditions:**

- (Step 1) The user is successfully logged into the application and a session is established.
- (Steps 2, 3, 4) The user is not logged in and remains on the sign-in page to correct their input or address the error.
