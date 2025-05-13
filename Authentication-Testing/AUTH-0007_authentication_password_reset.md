## **AUTH-0007:** Authentication - Password Reset

> **Summary:** Verify that a user who has forgotten their password can request a password reset link and subsequently set a new password. <br>

**Preconditions:**

- The user is on the "Forgot Password" or "Reset Password" page.
- The application's authentication and email services are operational.
- For password reset link requests, a user account with the provided email must exist.
- For setting a new password, the user must have a valid, unexpired password reset token (typically accessed via a link from email).

**Test Steps:**

| \# | Step Description (Forgot Password - Requesting Link)                                                                  | Expected Result (Forgot Password - Requesting Link)                                                                                                            |
|----|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A user who has forgotten their password enters their registered email address into the "Forgot Password" form and submits. | The system confirms the request (e.g., "If an account exists for this email, a password reset link has been sent.") An email containing a unique password reset link is sent to the user's registered email address. |
| 2  | A user enters an email address that is not registered in the system into the "Forgot Password" form and submits.           | To prevent email enumeration, the system often displays a generic confirmation message similar to step 1 (e.g., "If an account exists..."). No email is sent. Or, it may display "Email not found." (Depends on security policy) |
| 3  | A user attempts to request a password reset without entering an email address.                                          | The system displays an error message, such as "Email is required."                                                                                               |
| **\#** | **Step Description (Reset Password - Setting New Password)**                                                              | **Expected Result (Reset Password - Setting New Password)**                                                                                                      |
| 4  | After clicking the reset link from their email, the user is taken to a "Reset Password" page. They enter a new, valid password and confirm it correctly, then submit. | The system updates the user's password successfully. The user is informed (e.g., "Your password has been updated successfully!") and typically redirected to the sign-in page. The old reset link becomes invalid. |
| 5  | On the "Reset Password" page, the user enters a new password but the confirmation password does not match, then submits.   | The system displays an error message, such as "Passwords do not match." The password is not updated.                                                           |
| 6  | On the "Reset Password" page, the user enters matching valid passwords, but an unexpected issue occurs with the authentication service when trying to update the password. | The system displays a user-friendly error message (e.g., "Failed to update password. Please try again.") The password is not updated.                           |

**Post-conditions:**

- (Forgot Password - Step 1) A password reset token is generated and associated with the user's account; an email is dispatched.
- (Reset Password - Step 4) The user's account password is changed. The user can now log in with their new password.
- In error cases or for non-existent emails, the user's password remains unchanged, and appropriate feedback is provided.
