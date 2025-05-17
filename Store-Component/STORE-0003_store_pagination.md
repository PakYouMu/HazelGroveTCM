## **STORE-0003:** Store - Pagination  

> **Summary:** Verify that product pagination works correctly.  <br>

**Preconditions:** 

- The store has enough products to trigger pagination.
- Pagination logic is implemented in the store component.

**Test Steps:** 

| \# | Step Description                   | Expected Result                            |
| -- | ---------------------------------- | ------------------------------------------ |
| 1 | Load a store with many products. | First page of product list is shown. |
| 2 | Click “Next” or "Prev" button. | New product entries appear. |
| 3 | Confirm correct page display. | Products from the next or previous page load correctly. |

**Post-conditions:**  

- Users can view different pages of products without data duplication or loss.
