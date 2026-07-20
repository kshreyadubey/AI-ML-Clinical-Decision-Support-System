# AYURA Schedule Rules

## Purpose

This document defines the rules for generating, validating, managing, and optimizing patient schedules.

AYURA uses these rules to coordinate appointments, therapies, consultations, and follow-ups while preventing scheduling conflicts and maintaining an efficient patient journey.

---

# Core Principle

Every patient should have a clear, conflict-free, and optimized schedule.

Schedules should maximize treatment effectiveness while respecting healthcare professionals, departments, rooms, and patient availability.

---

# Schedule Objectives

AYURA should:

- Prevent scheduling conflicts.
- Minimize patient waiting time.
- Coordinate multiple departments.
- Optimize resource utilization.
- Maintain treatment continuity.
- Support personalized patient care.

---

# Schedule Components

A patient schedule may contain:

- Doctor Consultations
- Yoga Sessions
- Diet Consultations
- Acupuncture Sessions
- Follow-up Consultations
- Review Appointments

Each component becomes an event within the patient's schedule.

---

# Schedule Lifecycle

Draft

↓

Validated

↓

Confirmed

↓

Active

↓

Completed

Schedules may also become:

- Modified
- Cancelled

---

# Schedule Validation Rules

Before confirming a schedule, AYURA must verify:

- Patient availability
- Healthcare professional availability
- Room availability
- Appointment duration
- No overlapping events
- Valid workflow sequence

Schedules failing validation must not be confirmed.

---

# Conflict Detection

AYURA must detect:

- Double-booked patients
- Double-booked healthcare professionals
- Room conflicts
- Overlapping appointments
- Duplicate sessions
- Invalid workflow order

Every detected conflict should be reported before schedule confirmation.

---

# Schedule Optimization

AYURA should attempt to:

- Reduce patient movement.
- Reduce idle waiting time.
- Group related appointments.
- Maintain logical treatment order.
- Improve department coordination.

Optimization must never compromise patient safety.

---

# Schedule Modification

Schedules may be modified when:

- Treatment plans change.
- Healthcare professional requests changes.
- Patient requests changes.
- Resource availability changes.
- Operational conflicts occur.

Every modification should be recorded.

---

# Schedule Cancellation

A schedule or schedule item may be cancelled only by an authorized user.

Cancellation must record:

- User
- Reason
- Timestamp

Cancelled events remain in the audit history.

---

# Daily Schedule

Each day, AYURA should generate:

- Patient Schedule
- Doctor Schedule
- Yoga Schedule
- Dietitian Schedule
- Acupuncture Schedule

Schedules should reflect the latest approved treatment plan.

---

# Schedule Integrity

Schedules should always be:

- Accurate
- Complete
- Conflict-free
- Traceable
- Up-to-date

---

# Exception Handling

If scheduling cannot be completed, AYURA should:

- Identify the conflict.
- Explain the reason.
- Suggest available alternatives.
- Await user confirmation before applying changes.

---

# Schedule Statement

> AYURA coordinates multidisciplinary patient schedules by ensuring every appointment is validated, conflict-free, optimized, and aligned with the patient's treatment plan, enabling efficient and continuous healthcare delivery.