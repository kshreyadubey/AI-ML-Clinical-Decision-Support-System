"""
monitoring_agent.py

AYURA Monitoring Agent

Responsible for:
- Monitoring patient progress
- Workflow monitoring
- Documentation monitoring
- Therapy monitoring
- Appointment monitoring
- Clinical alerts
- Detecting missing information

NOTE:
This agent observes and reports.
It never makes clinical decisions.
"""

from datetime import datetime
from typing import Dict, List

from ayura.memory.memory_manager import memory_manager


class MonitoringAgent:
    """
    Monitoring Intelligence Agent.

    Continuously evaluates runtime information
    and identifies situations requiring attention.
    """

    def __init__(self):
        self.memory = memory_manager
        self.alerts: List[Dict] = []

    # --------------------------------------------------
    # Patient Monitoring
    # --------------------------------------------------

    def monitor_patient(self) -> Dict:

        return {
            "patient": self.memory.patient.get_patient_id(),
            "clinical": self.memory.clinical.summary(),
            "workflow": self.memory.workflow.summary(),
        }

    # --------------------------------------------------
    # Workflow Monitoring
    # --------------------------------------------------

    def monitor_workflow(self) -> Dict:

        return self.memory.workflow.summary()

    # --------------------------------------------------
    # Documentation Monitoring
    # --------------------------------------------------

    def monitor_documentation(self) -> Dict:

        notes = len(self.memory.clinical.notes)

        return {
            "notes": notes,
            "status": (
                "AVAILABLE"
                if notes > 0
                else "NO_DOCUMENTATION"
            )
        }

    # --------------------------------------------------
    # Alerts
    # --------------------------------------------------

    def raise_alert(
        self,
        level: str,
        message: str
    ):

        self.alerts.append({
            "level": level.upper(),
            "message": message,
            "timestamp": datetime.utcnow()
        })

    def get_alerts(self):

        return self.alerts

    def clear_alerts(self):

        self.alerts.clear()

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self) -> bool:

        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        return {
            "patient": self.memory.patient.get_patient_id(),
            "alerts": len(self.alerts),
            "workflow": self.memory.workflow.summary(),
            "clinical": self.memory.clinical.summary(),
        }

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.alerts.clear()

    def __repr__(self):

        return "<MonitoringAgent>"


# Singleton
monitoring_agent = MonitoringAgent()