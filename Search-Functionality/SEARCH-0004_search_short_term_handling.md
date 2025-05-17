## **SEARCH-0004:** Search - Short Term Handling  

> **Summary:** Verify that short search terms (≤3 chars) only search products as implemented.  <br>

**Preconditions:** 

- Short term threshold is defined in the search logic (e.g., ≤3 characters).
- Products exist that match short search terms.
- Search logic excludes stores for short terms.

**Test Steps:** 

| \# | Step Description                                  | Expected Result                          |
| -- | ------------------------------------------------- | ---------------------------------------- |
| 1  | Open the search interface. | Search bar appears. |
| 2  | Input a 3-character or shorter term (e.g., "pen") | Search begins automatically or on submit |
| 3  | Check the result set. | Only product results are returned. |
| 4  | Ensure no store results are listed. | Store results are excluded. |

**Post-conditions:**  

- Only product results are shown for short terms (e.g., “pen”).
- Search UI remains functional.
