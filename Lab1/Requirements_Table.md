# Requirements Table — Customizable Subscription Box Scheduler
**Problem Statement #35 | Retail, E-Commerce & Finance**
**SRN:** PES1UG24CS525

---

## Functional Requirements

| ID | Description | Priority | Acceptance Criteria | Rationale |
|----|--------------|----------|----------------------|-----------|
| **FR-001** | The system shall allow a Subscriber to swap items in their monthly box, filtered by their saved preference tags, up to 48 hours prior to the monthly billing renewal date. | High | **Pass:** Selection is updated and the fulfillment manifest reflects the new items before the cutoff. **Fail:** System accepts or silently drops a swap request after the 48-hour cutoff. | Customers need flexibility to tailor recurring deliveries to changing tastes without having to cancel and re-subscribe, which directly affects retention. |
| **FR-002** | The system shall allow a Subscriber to pause or skip exactly one upcoming billing cycle without cancelling the underlying subscription. | High | **Pass:** No charge is generated and no box is shipped for the skipped cycle; the subscription auto-resumes on the following cycle. **Fail:** Subscriber is billed or a box is shipped for a cycle marked as skipped. | Pausing (instead of forcing cancellation) reduces involuntary churn during months a subscriber doesn't want a box. |
| **FR-003** | The system shall allow a Subscriber to create, edit, or remove preference tags (e.g., "vegan," "sci-fi," "dark roast") that are used to filter the catalog of swappable items shown to them. | Medium | **Pass:** Updated tags immediately change the set of items offered during customization. **Fail:** Catalog shown to the subscriber does not reflect the latest saved tags. | Preference tags are the mechanism that makes each box "customizable," so they must stay in sync with what the subscriber is shown. |
| **FR-004** | The system shall automatically send a reminder notification (email/SMS) to a Subscriber 72 hours before renewal if no customization action has been taken for the upcoming cycle. | Medium | **Pass:** Notification is sent exactly once per cycle to subscribers who haven't customized, and never to those who have. **Fail:** Notification is missed, duplicated, or sent to subscribers who already customized. | Reduces the number of subscribers who miss the 48-hour customization/pause window purely due to forgetfulness. |
| **FR-005** | The system shall allow a Fulfillment Lead to generate and export a fulfillment manifest (packing list + shipping labels) for all active, non-paused subscriptions in the current billing cycle. | High | **Pass:** Exported manifest includes every active subscription's final item selection and a valid shipping label. **Fail:** Manifest omits an active subscription or includes one that was paused/skipped. | Warehouse operations depend on an accurate, complete manifest to pack and ship the correct boxes on schedule. |

---

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|----|------|--------------|----------|----------------------|-----------|
| **NFR-001** | Performance | The fulfillment manifest generator must export shipping labels for 10,000 monthly boxes in under 1 minute. | High | **Pass:** Benchmark tests confirm export completes within 60 seconds for a 10,000-box batch. **Fail:** Export exceeds 60 seconds or times out under simulated peak load. | Fulfillment runs on a tight warehouse schedule; slow
