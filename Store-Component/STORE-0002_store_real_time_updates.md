## **STORE-0002:** Store - Real-time Updates  

> **Summary:** Verify that store data updates in real-time when changes occur.  <br>

**Preconditions:** 

- Store component supports real-time updates (via WebSockets).
- Store data is changed externally (via system update).

**Test Steps:** 

| \# | Step Description                           | Expected Result                                         |
| -- | ------------------------------------------ | ------------------------------------------------------- |
| 1  | Load a store page/component. | Current store data is displayed. |
| 2  | Trigger or simulate external store update. | A field (e.g., product or status) is updated in backend. |
| 3  | Wait for real-time mechanism to reflect it. | Store component shows updated data without reload. |

**Post-conditions:**  

- Store data in the component reflects the new updates without manual refresh.
