## **AUTH-0001:** Authentication - Email Validation

> **Summary:** Ensure the system correctly validates email address formats provided by users during sign-up and sign-in. <br>

**Preconditions:**

- The user is on the sign-up or sign-in page of the application.
- The application's authentication services are operational.

**Test Steps:**

| \# | Step Description                                                                              | Expected Result                                                                                     |
|----|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 1  | A new user attempts to sign up by entering an email address in an invalid format (e.g., "user@domain", "userdomain.com", "user@.com") along with other required valid sign-up details. | The system displays an error message on the sign-up page, such as "Invalid email address," and does not proceed with account creation. |
| 2  | An existing or new user attempts to sign in by entering an email address in an invalid format along with a password. | The system displays an error message on the sign-in page, such as "Invalid email address," and does not attempt to authenticate the user. |

**Post-conditions:**

- The user's account is not created (for sign-up attempts).
- The user is not logged into the application.
- The user remains on the respective sign-up or sign-in page with an opportunity to correct their input.