"""
risk_agent.py

AYURA Risk Agent

Responsible for:
- Identifying clinical risks
- Detecting workflow risks
- Detecting scheduling conflicts
- Identifying missing information
- Detecting documentation gaps

NOTE:
This agent identifies risks only.
Final decisions always remain with healthcare professionals.
"""

from datetime import datetime
from typing import Dict, List

from ayura.memory.memory_manager import memory_manager


class RiskAgent:
    """
    Risk Intelligence Agent.

    Continuously evaluates runtime context
    for potential risks.
    """

    def __init__(self):
        self.memory = memory_manager
        self.risks: List[Dict] = []

    # --------------------------------------------------
    # Risk Management
    # --------------------------------------------------

    def add_risk(
        self,
        category: str,
        level: str,
        description: str
    ):
        """
        Register a detected risk.
        """

        self.risks.append({
            "category": category,
            "level": level.upper(),
            "description": description,
            "timestamp": datetime.utcnow()
        })

    def get_risks(self):

        return self.risks

    def clear_risks(self):

        self.risks.clear()

    # --------------------------------------------------
    # Clinical Risk
    # --------------------------------------------------

    def clinical_risk(self):

        clinical = self.memory.clinical.summary()

        if not clinical.get("diagnosis"):
            self.add_risk(
                "Clinical",
                "Medium",
                "Diagnosis not available."
            )

        if not clinical.get("treatment_plan"):
            self.add_risk(
                "Clinical",
                "Medium",
                "Treatment plan not available."
            )

    # --------------------------------------------------
    # Documentation Risk
    # --------------------------------------------------

    def documentation_risk(self):

        if len(self.memory.clinical.notes) == 0:
            self.add_risk(
                "Documentation",
                "Low",
                "No clinical notes available."
            )

    # --------------------------------------------------
    # Workflow Risk
    # --------------------------------------------------

    def workflow_risk(self):

        workflow = self.memory.workflow.summary()

        if workflow["status"] == "NOT_STARTED":
            self.add_risk(
                "Workflow",
                "Low",
                "Workflow has not started."
            )

    # --------------------------------------------------
    # Complete Assessment
    # --------------------------------------------------

    def assess(self):

        self.clear_risks()

        self.clinical_risk()
        self.documentation_risk()
        self.workflow_risk()

        return self.summary()

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        return {
            "patient": self.memory.patient.get_patient_id(),
            "total_risks": len(self.risks),
            "risks": self.risks
        }

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self):

        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.risks.clear()

    def __repr__(self):

        return f"<RiskAgent risks={len(self.risks)}>"


# Singleton
risk_agent = RiskAgent()