"""
therapy_agent.py

AYURA Therapy Agent

Responsible for:
- Therapy planning
- Therapy scheduling support
- Therapy progress tracking
- Therapy recommendations
- Therapy completion
- Therapy validation
"""

from typing import Dict, List

from ayura.memory.memory_manager import memory_manager


class TherapyAgent:
    """
    Therapy Coordination Agent.

    Coordinates patient therapies and maintains
    therapy-related runtime context.

    Therapy decisions remain with healthcare
    professionals.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Therapy Plan
    # --------------------------------------------------

    def get_plan(self) -> Dict:
        """
        Return current therapy plan.
        """

        return {
            "therapies": self.memory.clinical.summary().get(
                "therapies", []
            )
        }

    # --------------------------------------------------
    # Therapy Management
    # --------------------------------------------------

    def add_therapy(self, therapy: str):
        """
        Add therapy to current treatment.
        """

        self.memory.clinical.add_therapy(therapy)

    def remove_therapy(self, therapy: str):
        """
        Remove therapy from current treatment.
        """

        self.memory.clinical.remove_therapy(therapy)

    def list_therapies(self) -> List[str]:
        """
        Return all active therapies.
        """

        return self.memory.clinical.summary().get(
            "therapies", []
        )

    # --------------------------------------------------
    # Progress
    # --------------------------------------------------

    def therapy_progress(self) -> Dict:

        return {
            "patient": self.memory.patient.get_patient_id(),
            "therapies": self.list_therapies(),
            "workflow": self.memory.workflow.get_current_step(),
        }

    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------

    def recommend(self) -> Dict:
        """
        Therapy recommendations are generated
        by the reasoning engine.
        """

        return {
            "status": "available",
            "message": (
                "Therapy recommendations are provided "
                "by the reasoning engine."
            )
        }

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self) -> bool:
        """
        Ensure a patient is loaded before
        therapy operations.
        """

        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.memory.clinical.therapies.clear()

    def __repr__(self):
        return "<TherapyAgent>"


# Singleton
therapy_agent = TherapyAgent()