## **SEARCH-0001:** Search - Product Search  

> **Summary:** Verify that product search returns correct results based on name.  <br>

**Preconditions:** 

- The web app is running and connected to the backend.
- The product database contains products with distinct and searchable names.
- User is authenticated.

**Test Steps:** 

| \# | Step Description                      | Expected Result                                  |
| -- | ------------------------------------- | ------------------------------------------------ |
| 1  | Navigate to the web app's search page. | Search interface is displayed. |
| 2  | Enter a full or partial product name. | Suggestions or search activation appears. |
| 3  | Submit the search query. | Product results matching the input are displayed. |
| 4  | Observe the results. | Only relevant product matches are shown. |

**Post-conditions:**  

- The product search results are displayed correctly based on the entered name.
- Irrelevant products are not shown.
- UI updates without errors.
