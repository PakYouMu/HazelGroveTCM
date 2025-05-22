## **SEARCH-0003:** Search - Combined Search  

> **Summary:** Verify that combined search returns both products and stores correctly.  <br>

**Preconditions:** 

- Both product and store datasets are available and searchable.
- Combined search mode is implemented and active.

**Test Steps:** 

| \# | Step Description                         | Expected Result                                           |
| -- | ---------------------------------------- | --------------------------------------------------------- |
| 1  | Access the search bar. | UI for combined search is shown. |
| 2  | Enter a term that could match both types. | Search term is accepted and search begins. |
| 3  | View the output. | Product and store results are displayed in grouped format. |
| 4  | Validate relevance of both sets. | Only correct and matching entries for both are included. |

**Post-conditions:**  

- Both product and store matches are shown in a distinguishable format (e.g., icons or labels).
- Results are grouped or visually separated.
- No backend errors occur.
