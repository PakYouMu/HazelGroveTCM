## **AUTH-0008:** Authentication - Rate Limiting

> **Summary:** Ensure the system provides protection against brute-force attacks by limiting the number of repeated, unsuccessful authentication attempts (e.g., sign-in) from a single source within a short time period. <br>

**Preconditions:**

- The user is attempting to perform an action subject to rate limiting, such as signing in.
- The application's authentication services are operational and have rate-limiting policies configured.

**Test Steps:**

| \# | Step Description                                                                                                | Expected Result                                                                                                                                                                                             |
|----|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | A user (or automated script) makes multiple consecutive unsuccessful sign-in attempts with incorrect credentials for a valid or invalid account, exceeding the configured rate limit (e.g., more than 5 attempts in 1 minute). | After exceeding the allowed number of attempts, the system temporarily blocks further sign-in attempts from that source (IP address or user account). The user is presented with an error message, such as "Too many sign-in attempts. Please try again later." or an HTTP 429 error is returned by the API. |

**Post-conditions:**

- Further authentication attempts from the rate-limited source are temporarily denied.
- Legitimate users who were temporarily locked out can regain access after the lockout period expires.
- The system remains stable and protected against excessive login attempts.
- **Note:** The exact rate limits (number of attempts, time window) are defined by the authentication provider (e.g., Supabase) and application configuration.