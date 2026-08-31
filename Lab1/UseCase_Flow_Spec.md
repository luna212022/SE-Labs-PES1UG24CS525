# Use-Case Flow Specification

## Use Case: Customize Box Selection

**ID:** UC-01
**Related Requirement:** FR-001
**Primary Actor:** Subscriber
**Secondary/Included Use Case:** Validate Customization Window («include»)
**Trigger:** Subscriber logs into the portal and selects "Customize my box" during an active billing cycle.

---

### Preconditions
- The Subscriber has an active, non-cancelled subscription.
- The Subscriber is authenticated (logged in) to the portal.
- The current billing cycle's renewal date is more than 0 hours away (i.e., the cycle has not yet renewed).
- At least one item eligible for the Subscriber's saved preference tags exists in the catalog.

### Postconditions
**Success:**
- The Subscriber's box selection for the upcoming cycle is updated and persisted.
- The fulfillment manifest for the upcoming cycle is refreshed to reflect the new selection.
- A confirmation is displayed to the Subscriber and logged for audit purposes.

**Failure:**
- No change is made to the existing box selection.
- The Subscriber is shown an explanatory message (e.g., window closed, item unavailable).

---

### Main Success Scenario
1. Subscriber selects "Customize my box" from their account dashboard.
2. System invokes **Validate Customization Window** («include») to confirm the current time is more than 48 hours before the renewal date.
3. System retrieves the catalog of items filtered by the Subscriber's saved preference tags.
4. System displays the current box selection alongside eligible swap options.
5. Subscriber selects one or more replacement items and confirms the change.
6. System validates that the new selection meets box composition rules (e.g., item count, category limits).
7. System saves the updated selection against the Subscriber's upcoming cycle.
8. System refreshes the draft fulfillment manifest entry for this Subscriber.
9. System displays a confirmation message with the finalized item list.

### Alternate Flow A1: Customization Window Has Closed
*Triggered at step 2, when Validate Customization Window fails.*

1. System determines the current time is within 48 hours of the renewal date (or past it).
2. System blocks the customization action and displays a message: "Customization is locked for this cycle; changes will apply to your next box."
3. System offers the Subscriber the option to view (read-only) the box that will ship, or to set preferences for the *next* cycle instead.
4. Use case ends without modifying the current cycle's selection.

---

**Notes:** This use case includes "Validate Customization Window" because the same 48-hour check is reused by "Pause / Skip Delivery" (UC-02), so it is factored out as a separate, always-executed sub-use-case rather than duplicated logic.
