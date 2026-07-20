"""
report_agent.py

AYURA Report Agent

Responsible for:
- Patient reports
- Clinical summaries
- Treatment reports
- Progress reports
- Department reports
- Discharge summaries

NOTE:
This agent prepares report data.
Actual PDF/Excel generation is handled
by the reporting service.
"""

from datetime import datetime
from typing import Dict

from ayura.memory.memory_manager import memory_manager


class ReportAgent:
    """
    Report Intelligence Agent.

    Collects information from memory
    and prepares structured reports.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Patient Report
    # --------------------------------------------------

    def patient_report(self) -> Dict:

        return {
            "patient_id": self.memory.patient.get_patient_id(),
            "clinical": self.memory.clinical.summary(),
            "workflow": self.memory.workflow.summary(),
            "generated_at": datetime.utcnow(),
        }

    # --------------------------------------------------
    # Clinical Report
    # --------------------------------------------------

    def clinical_report(self) -> Dict:

        return {
            "patient_id": self.memory.patient.get_patient_id(),
            "clinical": self.memory.clinical.summary(),
            "generated_at": datetime.utcnow(),
        }

    # --------------------------------------------------
    # Progress Report
    # --------------------------------------------------

    def progress_report(self) -> Dict:

        clinical = self.memory.clinical.summary()

        return {
            "progress": clinical.get("progress"),
            "therapies": clinical.get("therapies"),
            "notes": clinical.get("notes"),
            "generated_at": datetime.utcnow(),
        }

    # --------------------------------------------------
    # Workflow Report
    # --------------------------------------------------

    def workflow_report(self) -> Dict:

        return self.memory.workflow.summary()

    # --------------------------------------------------
    # Department Report
    # --------------------------------------------------

    def department_report(self, department: str) -> Dict:

        return {
            "department": department,
            "status": "AVAILABLE",
            "generated_at": datetime.utcnow(),
        }

    # --------------------------------------------------
    # Discharge Report
    # --------------------------------------------------

    def discharge_report(self) -> Dict:

        return {
            "patient_id": self.memory.patient.get_patient_id(),
            "clinical": self.memory.clinical.summary(),
            "workflow": self.memory.workflow.summary(),
            "status": "READY",
            "generated_at": datetime.utcnow(),
        }

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self) -> bool:

        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):
        """
        No runtime state maintained.
        """
        pass

    def __repr__(self):

        return "<ReportAgent>"


# Singleton
report_agent = ReportAgent()