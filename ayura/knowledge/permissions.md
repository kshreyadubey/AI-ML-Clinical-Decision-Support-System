# AYURA Permission Knowledge

## Purpose

This document defines the Role-Based Access Control (RBAC) model used by AYURA.

Permissions determine which users can view, create, modify, approve, or delete information within the system. AYURA enforces these permissions before executing any action to ensure security, privacy, and accountability.

---

# Core Principle

Every action must be performed by an authorized user.

AYURA verifies permissions before executing any request.

No user may access information or perform actions beyond their assigned role.

---

# Permission Levels

AYURA uses four permission levels:

## View

Allows a user to read information.

Examples:

- View patient profile
- View appointments
- View schedules
- View reports

---

## Create

Allows a user to add new information.

Examples:

- Register patient
- Create appointment
- Add therapy notes
- Create treatment plan

---

## Update

Allows a user to modify existing information.

Examples:

- Update patient details
- Modify treatment plan
- Update diet
- Edit appointment

---

## Approve

Allows a user to authorize critical actions.

Examples:

- Approve treatment plan
- Approve discharge
- Approve AI recommendation
- Approve workflow completion

---

# Doctor Permissions

Doctors can:

- View assigned patient records
- View complete medical history
- Create treatment plans
- Update treatment plans
- Review AI recommendations
- Generate prescriptions
- Approve patient discharge
- Record consultation notes
- View reports

Doctors cannot:

- Modify audit logs
- Change system configuration
- Modify AI core settings

---

# Yoga Therapist Permissions

Yoga Therapists can:

- View assigned patients
- View therapy schedules
- Record attendance
- Add therapy notes
- Record observations
- Update therapy progress

Yoga Therapists cannot:

- Diagnose patients
- Modify treatment plans
- Approve discharge
- Access unrelated patient records

---

# Dietitian Permissions

Dietitians can:

- View assigned patients
- View treatment instructions
- Assign diets
- Modify diet plans
- Record nutrition notes
- Monitor diet compliance

Dietitians cannot:

- Diagnose patients
- Modify medical treatment plans
- Approve discharge

---

# Acupuncture Specialist Permissions

Acupuncture Specialists can:

- View assigned patients
- View therapy schedules
- Record treatment sessions
- Add observations
- Update therapy progress

Acupuncture Specialists cannot:

- Diagnose patients
- Modify treatment plans
- Approve discharge

---

# Developer Permissions

Developers can:

- Configure AYURA
- Manage AI settings
- Monitor system health
- View logs
- View audit records
- Deploy updates
- Maintain databases
- Configure integrations

Developers cannot:

- Make clinical decisions
- Modify patient records without authorization
- Approve treatments
- Approve discharge

---

# AYURA Permissions

AYURA can:

- Read authorized information
- Generate recommendations
- Coordinate workflows
- Generate schedules
- Create reports
- Maintain documentation
- Send notifications
- Monitor workflows
- Detect conflicts

AYURA cannot:

- Diagnose independently
- Prescribe medication
- Override healthcare professionals
- Bypass permission rules
- Modify audit history
- Execute unauthorized actions

---

# Permission Validation

Before every action, AYURA verifies:

1. User identity
2. User role
3. Requested action
4. Resource ownership
5. Required permission
6. Workflow state
7. Authorization

If any validation fails, the action is denied.

---

# Access Principles

Permissions follow these principles:

- Least Privilege
- Need-to-Know Access
- Role-Based Access
- Secure by Default
- Accountability
- Privacy First

---

# Permission Inheritance

Higher roles may inherit appropriate permissions from lower roles only when necessary and explicitly configured.

No user automatically receives unrestricted access.

---

# Audit Requirement

Every permission-protected action must record:

- User
- Role
- Action
- Resource
- Timestamp
- Status (Allowed / Denied)
- Reason (if denied)

---

# Permission Statement

> AYURA enforces role-based permissions to ensure that every action is performed only by authorized users. By validating identity, role, and workflow context before execution, AYURA protects patient privacy, maintains clinical integrity, and supports secure, accountable healthcare operations.