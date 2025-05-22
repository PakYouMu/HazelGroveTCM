## **SEARCH-0005:** Search - Empty Results Handling  

> **Summary:** Verify that empty search results are handled gracefully.  <br>

**Preconditions:** 

- Search backend is reachable.
- No products or stores match the given search term.

**Test Steps:** 

| \# | Step Description                   | Expected Result                                |
| -- | ---------------------------------- | ---------------------------------------------- |
| 1 | Use the search bar.                 | Search interface displays properly. |
| 2 | Enter a random or nonsensical term. | Search runs with no database matches. |
| 3 | View the results section.           | A friendly "No results found" message is shown. |
| 4 | Try searching again.                | Search bar remains usable and functional. |

**Post-conditions:**  

- A “no results found” message or UI is displayed.
- No blank or broken UI components appear.
- User can enter a new search term without refreshing the page.
