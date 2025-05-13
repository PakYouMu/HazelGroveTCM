## **AUTH-0004:** Authentication - Sign Up Flow

> **Summary:** Verify a new user can successfully create an account, and the system correctly handles attempts to sign up with an existing email or when backend services encounter issues. <br>

**Preconditions:**

- The user is on the sign-up page.
- The application's authentication and database services are operational.

**Test Steps:**

| \# | Step Description                                                                    | Expected Result                                                                                                                               |
|----|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A new user provides a unique, valid email address, a strong password (meeting criteria), and all other required information (username, affiliation) and submits the sign-up form. | The system creates a new user account. The user is typically redirected to the sign-in page or a confirmation page, with a message indicating successful sign-up and to check their email for verification. |
| 2  | A user attempts to sign up using an email address that already belongs to an existing account. | The system displays an error message on the sign-up page, such as "Email is already registered," and does not create a duplicate account.      |
| 3  | A new user provides valid sign-up information, but an unexpected issue occurs with the authentication service during the account creation process. | The system displays a user-friendly error message (e.g., "Sign up failed. Please try again later.") and does not create the account.               |
| 4  | A new user attempts to sign up but omits one or more required fields (e.g., does not enter a username). | The system displays an error message on the sign-up page, such as "All fields are required," prompting the user to complete the form.        |

**Post-conditions:**

- (Step 1) A new user account is created in the system, awaiting email verification if applicable.
- (Steps 2, 3, 4) No new account is created. The user remains on the sign-up page to address the issue.
