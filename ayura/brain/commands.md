# AYURA Commands

## Purpose

This document defines every command, intent, and action that AYURA understands and can execute.

A command represents a user request that initiates one or more workflows.

Commands are categorized according to workspaces and hospital operations.

---

# Command Structure

Every command consists of:

- Command Name
- Intent
- Authorized Users
- Required Inputs
- Workflow Triggered
- Expected Output

---

# Doctor Commands

## Register Patient

Intent:
Create a new patient profile.

Required Inputs:

- Personal Information
- Medical History
- Contact Details

Triggers:

Patient Registration Workflow

Output:

- Patient ID
- Initial Patient Record

---

## Open Patient

Intent:

Retrieve an existing patient's complete profile.

Output:

Patient Dashboard

---

## Update Patient

Intent:

Modify patient information.

Requires:

Reason for modification.

---

## Create Treatment Plan

Intent:

Assign therapies and treatment recommendations.

Output:

Treatment Plan

---

## Assign Diet Plan

Intent:

Assign a hospital diet from the diet library.

---

## Review AI Recommendations

Intent:

View AI-generated treatment suggestions.

---

## Generate Master Schedule

Intent:

Generate an optimized multidisciplinary schedule.

---

## View Daily Brief

Intent:

Generate today's clinical summary.

---

## Record Consultation

Intent:

Save consultation notes.

---

## Modify Treatment

Intent:

Update therapies.

Requires:

Reason for modification.

---

## Discharge Patient

Intent:

Complete treatment.

Generate:

- Discharge Report
- Final Summary

---

# Yoga Therapist Commands

- View Assigned Patients
- Start Session
- Complete Session
- Record Attendance
- Record Progress
- Add Therapy Notes
- Recommend Modification

---

# Dietitian Commands

- Create Diet Plan
- Update Diet Plan
- Delete Diet Plan
- View Diet Library
- Generate Nutrition Report
- View Diet Analytics

---

# Acupuncture Commands

- View Patients
- Start Session
- Complete Session
- Record Observations
- Update Treatment Notes

---

# Patient Commands

- View Schedule
- View Treatment Plan
- Update Daily Progress
- Record Symptoms
- Submit Feedback
- Chat with AYURA
- View Treatment History
- Download Reports

---

# Administrator Commands

- Manage Users
- Manage Roles
- View Audit Logs
- Configure Hospital Settings
- Manage Departments
- View System Reports

---

# Developer Commands

- View AI Logs
- Monitor Agent Health
- View Memory Status
- View Model Performance
- Reload Brain
- Reload Knowledge
- Manage AI Configuration

---

# AI Internal Commands

These commands are not directly available to users.

- Load Brain
- Load Knowledge
- Retrieve Memory
- Validate Permissions
- Validate Workflow
- Execute Reasoning
- Create Plan
- Execute Workflow
- Update Memory
- Record Audit
- Generate Response
- Notify Departments
- Self Verification

---

# Command Validation

Before executing any command, AYURA verifies:

- User identity
- User permissions
- Patient context (if required)
- Workflow eligibility
- Required inputs

---

# Command Execution Flow

Receive Command

↓

Validate User

↓

Verify Permission

↓

Identify Workflow

↓

Collect Inputs

↓

Execute Command

↓

Update Database

↓

Update Memory

↓

Record Audit

↓

Generate Response

---

# Command Statement

> Every command I execute must be validated, authorized, traceable, and aligned with hospital workflows while ensuring patient safety and professional clinical support.