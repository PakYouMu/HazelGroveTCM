## **SEARCH-0002:** Search - Store Search  

> **Summary:** Verify that store search returns correct results based on name.  <br>

**Preconditions:** 

- Store data is available in the backend.
- Store names are indexed or searchable.
- User has access to the search bar.

**Test Steps:** 

| \# | Step Description                     | Expected Result                            |
| ---| ------------------------------------ | ------------------------------------------ |
| 1  | Go to the search interface. | Search bar is available. |
| 2  | Input a store name or partial string | Search engages and shows potential results |
| 3  | Press Enter or tap the search button | Store results related to the input appear. |
| 4  | Confirm that only stores are listed. | No unrelated products are shown. |

**Post-conditions:**  

- Relevant stores are displayed in the results.
- Product results (if any) are excluded unless specified.
- Store names match the search term (case-insensitive, partial matches allowed).