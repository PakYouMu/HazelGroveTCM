## **STORE-0005:** Store - Edit Mode  

> **Summary:** Verify that store edit mode can be toggled correctly.  <br>

**Preconditions:** 

- Edit mode is implemented and accessible.
- User is authenticated and authorized to edit.
- An existing store is clicked or currently accessed through the store card.

**Test Steps:** 
| \# | Step Description                     | Expected Result                                        |
| -- | ------------------------------------ | ------------------------------------------------------ |
| 1  | Access a store as an authorized user. | Store component loads normally. |
| 2  | Click the “Edit Products” toggle button. | Component enters edit mode (input fields appear, etc.). |
| 3  | Toggle edit mode off. | Component returns to view-only mode. |

**Post-conditions:**  

- Edit mode can be enabled/disabled and reflects in UI and form controls.
