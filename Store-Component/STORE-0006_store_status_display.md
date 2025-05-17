## **STORE-0006:** Store - Status Display  

> **Summary:** Verify that store open/closed status is displayed correctly.  <br>

**Preconditions:** 

- Store block is clicked by user.
- Store card is displayed from user click or entering user search.
- Store records include a status card.
- Displayed status is either open or closed.

**Test Steps:** 

| \# | Step Description                    | Expected Result                                          |
| -- | ----------------------------------- | -------------------------------------------------------- |
| 1 | Load a store component. | Current status (Open/Closed) is visible. |
| 2 | Simulate status change from backend | Backend store status is toggled. |
| 3 | Observe new status on UI. | UI reflects updated status in real-time or after refresh |

**Post-conditions:**  

- Status (Open/Closed) is visible and accurate in the store UI.