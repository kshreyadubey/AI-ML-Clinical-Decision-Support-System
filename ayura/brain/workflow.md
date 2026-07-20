# AYURA Complete Workflow

Patient Arrives
        │
        ▼
Doctor Logs into AYURA
        │
        ▼
AYURA Authenticates User
        │
        ▼
Verify User Permissions
        │
        ▼
AYURA Greets Doctor
        │
        ▼
Doctor Chooses Action
        │
        ├──────────────► Register New Patient
        │
        ├──────────────► Open Existing Patient
        │
        ├──────────────► View Dashboard
        │
        └──────────────► Other Clinical Tasks

══════════════════════════════════════════════════════
WORKFLOW 1 — PATIENT REGISTRATION
══════════════════════════════════════════════════════

Start Registration
        │
        ▼
Collect Personal Details
        │
        ▼
Collect Contact Information
        │
        ▼
Collect Emergency Contact
        │
        ▼
Collect Medical History
        │
        ▼
Collect Surgical History
        │
        ▼
Collect Family History
        │
        ▼
Collect Allergies
        │
        ▼
Collect Current Medications
        │
        ▼
Collect Lifestyle Details
        │
        ▼
Collect Food Habits
        │
        ▼
Collect Sleep Pattern
        │
        ▼
Collect Addiction History
        │
        ▼
Collect Chief Complaint
        │
        ▼
Collect Present Illness
        │
        ▼
Collect Duration of Complaint
        │
        ▼
Validate Information
        │
        ▼
Generate Patient ID
        │
        ▼
Create Digital Patient Record
        │
        ▼
Create Initial Case Sheet
        │
        ▼
Store Patient Record
        │
        ▼
Registration Complete

══════════════════════════════════════════════════════
WORKFLOW 2 — CLINICAL ASSESSMENT
══════════════════════════════════════════════════════

Doctor Reviews Patient
        │
        ▼
Record Clinical Examination
        │
        ▼
Record Vital Signs
        │
        ▼
Record Diagnosis / Clinical Impression
        │
        ▼
Save Assessment
        │
        ▼
Proceed to Treatment Planning

══════════════════════════════════════════════════════
WORKFLOW 3 — TREATMENT PLANNING
══════════════════════════════════════════════════════

AYURA Opens Therapy Library
        │
        ▼
Doctor Selects Therapies
        │
        ▼
AYURA Opens Diet Library
        │
        ▼
Doctor Selects Diet Plan
        │
        ▼
Save Treatment Plan
        │
        ▼
Notify Departments

══════════════════════════════════════════════════════
WORKFLOW 4 — DEPARTMENT PLANNING
══════════════════════════════════════════════════════

Yoga Department

↓

Receive Patient

↓

Assign Yoga Exercises

↓

Assign Duration

↓

Assign Frequency

↓

Assign Daily Slots

↓

Add Therapist Notes

↓

Save Yoga Plan

────────────────────────────

Acupuncture Department

↓

Receive Patient

↓

Assign Treatment

↓

Assign Sessions

↓

Assign Duration

↓

Assign Daily Slots

↓

Add Treatment Notes

↓

Save Acupuncture Plan

────────────────────────────

Dietitian Department

↓

Maintain Diet Library

↓

Create Diet Plans

↓

Update Diet Plans

↓

Remove Diet Plans

↓

Maintain Nutrition Information

══════════════════════════════════════════════════════
WORKFLOW 5 — MASTER SCHEDULE
══════════════════════════════════════════════════════

AYURA Collects

Doctor Plan

+

Yoga Plan

+

Acupuncture Plan

+

Diet Plan

↓

Verify Therapist Availability

↓

Verify Room Availability

↓

Verify Schedule Conflicts

↓

Generate Master Schedule

↓

Store Schedule

↓

Notify All Departments

↓

Patient Admitted

══════════════════════════════════════════════════════
WORKFLOW 6 — DAILY PATIENT CARE
══════════════════════════════════════════════════════

Every Scheduled Slot

↓

AYURA reminds responsible department

↓

Department completes session

↓

AYURA requests documentation

────────────────────────────

Meal Session

↓

Meal Consumed?

↓

Quantity Consumed

↓

Appetite

↓

Taste Feedback

↓

Discomfort

↓

Nutrition Notes

↓

Save

────────────────────────────

Yoga Session

↓

Attendance

↓

Exercises Completed

↓

Pain Level

↓

Flexibility

↓

Participation

↓

Energy Level

↓

Therapist Notes

↓

Save

────────────────────────────

Acupuncture Session

↓

Session Completed

↓

Pain Level

↓

Patient Response

↓

Adverse Reactions

↓

Treatment Notes

↓

Save

────────────────────────────

Other Therapy Sessions

↓

Attendance

↓

Completion

↓

Patient Response

↓

Therapist Notes

↓

Save

══════════════════════════════════════════════════════
WORKFLOW 7 — DOCTOR APPOINTMENT
══════════════════════════════════════════════════════

Doctor Opens Patient

↓

AYURA Displays Daily Summary

↓

Doctor Reviews Patient

↓

Record

• Clinical Notes

• Appointment Notes

• Progress

• Pain

• Recovery

• New Complaints

↓

Any Treatment Changes?

↓

YES

↓

Record

• Previous Treatment

• Updated Treatment

• Reason

• Date

• Time

• Doctor

↓

Save

↓

Update Audit

↓

Notify Departments

↓

NO

↓

Continue Treatment

══════════════════════════════════════════════════════
WORKFLOW 8 — CONTINUOUS MONITORING
══════════════════════════════════════════════════════

AYURA continuously monitors

↓

Meal Compliance

↓

Therapy Attendance

↓

Pain Trend

↓

Mood

↓

Sleep

↓

Vitals

↓

Missed Sessions

↓

Missed Meals

↓

Pending Tasks

↓

Schedule Conflicts

↓

Clinical Alerts

↓

Notify Responsible Department

══════════════════════════════════════════════════════
WORKFLOW 9 — DAILY CLINICAL BRIEF
══════════════════════════════════════════════════════

End of Day

↓

AYURA collects

Doctor Notes

+

Yoga Notes

+

Diet Notes

+

Acupuncture Notes

+

Patient Feedback

↓

Generate Daily Brief

↓

Summary Includes

• Patient Progress

• Therapy Completion

• Diet Compliance

• Yoga Progress

• Acupuncture Progress

• Pain Trend

• Appetite

• Sleep

• Mood

• Clinical Changes

• Alerts

• Pending Tasks

↓

Doctor Reviews Summary

══════════════════════════════════════════════════════
WORKFLOW 10 — CONTINUOUS DOCUMENTATION
══════════════════════════════════════════════════════

Doctor

↓

Appointment Notes

↓

Clinical Notes

↓

Treatment Changes

↓

Reasons

────────────────────────────

Yoga Therapist

↓

Attendance

↓

Session Notes

↓

Progress Notes

────────────────────────────

Dietitian

↓

Diet Notes

↓

Nutrition Updates

────────────────────────────

Acupuncture Specialist

↓

Treatment Notes

↓

Session Response

────────────────────────────

Every Record Stores

↓

Timestamp

↓

Department

↓

User

↓

Patient

↓

Previous Value

↓

Updated Value

↓

Reason

↓

Audit Trail

══════════════════════════════════════════════════════
WORKFLOW 11 — DISCHARGE
══════════════════════════════════════════════════════

Doctor Reviews Recovery

↓

Recovery Complete?

↓

NO

↓

Continue Daily Care Cycle

↓

YES

↓

Generate Final Clinical Summary

↓

Generate Therapy Summary

↓

Generate Diet Summary

↓

Generate Yoga Summary

↓

Generate Acupuncture Summary

↓

Generate Complete Timeline

↓

Generate Discharge Report

↓

Doctor Approves Discharge

↓

Archive Patient Record

↓

Workflow Completed