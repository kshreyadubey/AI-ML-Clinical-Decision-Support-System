"""
workflow_agent.py

AYURA Workflow Agent

Responsible for:
- Starting workflows
- Resuming workflows
- Completing workflows
- Tracking workflow progress
- Managing workflow state
- Coordinating workflow execution

NOTE:
This agent manages workflow execution only.
Business logic belongs to the Workflow Engine.
"""

from typing import Dict

from ayura.memory.memory_manager import memory_manager


class WorkflowAgent:
    """
    Workflow Coordination Agent.

    Manages the lifecycle of patient workflows
    and exposes workflow operations to AYURA.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Workflow Lifecycle
    # --------------------------------------------------

    def start(self, workflow_name: str):
        """
        Start a new workflow.
        """

        self.memory.start_workflow(workflow_name)

    def complete(self):
        """
        Complete the active workflow.
        """

        self.memory.complete_workflow()

    def cancel(self):
        """
        Cancel the active workflow.
        """

        self.memory.workflow.cancel_workflow()

    # --------------------------------------------------
    # Workflow Steps
    # --------------------------------------------------

    def current_step(self):

        return self.memory.workflow.get_current_step()

    def set_step(self, step: str):

        self.memory.workflow.set_current_step(step)

    def complete_step(self, step: str):

        self.memory.workflow.complete_step(step)

    def add_pending_step(self, step: str):

        self.memory.workflow.add_pending_step(step)

    def remove_pending_step(self, step: str):

        self.memory.workflow.remove_pending_step(step)

    # --------------------------------------------------
    # Resume
    # --------------------------------------------------

    def resume(self) -> Dict:
        """
        Resume the active workflow.
        """

        return {
            "workflow": self.memory.workflow.workflow_name,
            "status": self.memory.workflow.workflow_status,
            "current_step": self.current_step(),
            "progress": self.memory.workflow.progress(),
        }

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    def add_history(self, action: str):

        self.memory.workflow.add_history(action)

    # --------------------------------------------------
    # Progress
    # --------------------------------------------------

    def progress(self):

        return self.memory.workflow.progress()

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):

        return self.memory.workflow.summary()

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self):

        return self.memory.patient.is_loaded

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.memory.workflow.clear()

    def __repr__(self):

        return "<WorkflowAgent>"


# Singleton
workflow_agent = WorkflowAgent()