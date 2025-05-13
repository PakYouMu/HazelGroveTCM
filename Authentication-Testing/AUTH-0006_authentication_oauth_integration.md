## **AUTH-0006:** Authentication - OAuth Integration (Google)

> **Summary:** Verify that users can initiate the sign-in/sign-up process using their Google account. <br>

**Preconditions:**

- The user is on the sign-in or sign-up page where the "Sign in with Google" option is available.
- The application is correctly configured for Google OAuth with the authentication provider.

**Test Steps:**

| \# | Step Description                                                                     | Expected Result                                                                                                                                        |
|----|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A user clicks the "Sign in with Google" (or similar) button.                          | The user is redirected from the application to Google's authentication page, where they can select their Google account and grant permissions to the application. |
| 2  | A user clicks the "Sign in with Google" button, but an issue occurs during the initiation (e.g., misconfiguration, Google service temporarily unavailable). | The system displays a user-friendly error message on the application's sign-in page (e.g., "Could not connect to Google. Please try again."). The user is not redirected to Google. |

**Post-conditions:**

- (Step 1) The user is on Google's authentication domain. Upon successful Google authentication and authorization, they will be redirected back to the application's designated callback URL to complete the sign-in/sign-up process.
- (Step 2) The user remains within the application and is informed of the issue.