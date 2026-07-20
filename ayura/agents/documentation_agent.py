"""
documentation_agent.py

AYURA Documentation Agent

Responsible for:
- Clinical documentation
- Consultation notes
- Therapy notes
- Appointment notes
- Progress notes
- Discharge summaries
- Documentation validation
"""

from datetime import datetime
from typing import Dict, List

from ayura.memory.memory_manager import memory_manager


class DocumentationAgent:
    """
    Documentation Intelligence Agent.

    Responsible for creating and organizing
    clinical documentation.

    Permanent storage is handled by the
    documentation service layer.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Clinical Notes
    # --------------------------------------------------

    def add_clinical_note(self, note: str):

        self.memory.clinical.add_note(note)

    def get_clinical_notes(self) -> List[Dict]:

        return self.memory.clinical.notes

    # --------------------------------------------------
    # Therapy Notes
    # --------------------------------------------------

    def add_therapy_note(self, note: str):

        self.memory.clinical.add_note(
            f"[THERAPY] {note}"
        )

    # --------------------------------------------------
    # Appointment Notes
    # --------------------------------------------------

    def add_appointment_note(self, note: str):

        self.memory.clinical.add_note(
            f"[APPOINTMENT] {note}"
        )

    # --------------------------------------------------
    # Progress Notes
    # --------------------------------------------------

    def add_progress_note(self, note: str):

        self.memory.clinical.add_note(
            f"[PROGRESS] {note}"
        )

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def generate_summary(self) -> Dict:

        return {
            "patient_id": self.memory.patient.get_patient_id(),
            "notes": len(self.memory.clinical.notes),
            "workflow": self.memory.workflow.summary(),
            "generated_at": datetime.utcnow()
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

        self.memory.clinical.notes.clear()

    def __repr__(self):

        return "<DocumentationAgent>"


# Singleton
documentation_agent = DocumentationAgent()