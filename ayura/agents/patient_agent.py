"""
patient_agent.py

AYURA Patient Agent

Responsible for:
- Patient registration
- Patient profile management
- Patient lookup
- Patient timeline
- Patient context loading
- Admission & discharge support
"""

from typing import Dict, Optional

from ayura.memory.memory_manager import memory_manager


class PatientAgent:
    """
    Patient Management Agent.

    Handles all patient-related operations and
    provides patient context to AYURA.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Context
    # --------------------------------------------------

    def load_patient(self, patient_id: int):
        """
        Load the active patient into memory.
        """
        self.memory.load_patient(patient_id)

    def unload_patient(self):
        """
        Remove current patient from memory.
        """
        self.memory.clear_patient()

    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register_patient(self, patient_data: Dict):
        """
        Placeholder.

        Registration is handled by the service layer.
        """
        return {
            "status": "pending",
            "message": "Patient registration handled by services.",
            "patient": patient_data
        }

    # --------------------------------------------------
    # Profile
    # --------------------------------------------------

    def get_patient_profile(self):

        patient_id = self.memory.patient.get_patient_id()

        return {
            "patient_id": patient_id,
            "context": self.memory.patient.get_context()
        }

    # --------------------------------------------------
    # Timeline
    # --------------------------------------------------

    def get_patient_timeline(self):
        """
        Timeline generation will be handled
        by the reasoning/report engine.
        """

        return {
            "status": "available",
            "message": "Timeline generated from clinical history."
        }

    # --------------------------------------------------
    # Admission
    # --------------------------------------------------

    def admit_patient(self):
        return {
            "status": "pending",
            "message": "Admission handled by workflow engine."
        }

    # --------------------------------------------------
    # Discharge
    # --------------------------------------------------

    def discharge_patient(self):
        return {
            "status": "pending",
            "message": "Discharge handled by workflow engine."
        }

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self) -> bool:
        """
        Ensure an active patient exists.
        """
        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):
        self.memory.clear_patient()

    def __repr__(self):
        return "<PatientAgent>"


# Singleton
patient_agent = PatientAgent()