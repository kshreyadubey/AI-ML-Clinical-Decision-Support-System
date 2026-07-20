"""
learning_agent.py

AYURA Learning Agent

Responsible for:
- Recording user feedback
- Learning reusable workflow patterns
- Learning user preferences
- Capturing successful clinical workflows
- Providing learning insights

NOTE:
This agent never modifies historical records.
It only stores approved learning information.
"""

from typing import Dict, List

from ayura.memory.memory_manager import memory_manager


class LearningAgent:
    """
    Learning Intelligence Agent.

    Continuously improves AYURA by storing
    reusable knowledge and approved patterns.
    """

    def __init__(self):
        self.memory = memory_manager

    # --------------------------------------------------
    # Preferences
    # --------------------------------------------------

    def remember_preference(
        self,
        key: str,
        value
    ):

        self.memory.learning.remember_preference(
            key,
            value
        )

    def preferences(self):

        return self.memory.learning.preferences

    # --------------------------------------------------
    # Workflow Learning
    # --------------------------------------------------

    def learn_workflow(
        self,
        workflow: str,
        details: Dict
    ):

        self.memory.learning.remember_workflow(
            workflow,
            details
        )

    # --------------------------------------------------
    # Pattern Learning
    # --------------------------------------------------

    def learn_pattern(
        self,
        name: str,
        description: str
    ):

        self.memory.learning.remember_pattern(
            name,
            description
        )

    # --------------------------------------------------
    # Feedback
    # --------------------------------------------------

    def record_feedback(
        self,
        source: str,
        feedback: str
    ):

        self.memory.learning.add_feedback(
            source,
            feedback
        )

    # --------------------------------------------------
    # Lessons
    # --------------------------------------------------

    def record_lesson(
        self,
        lesson: str
    ):

        self.memory.learning.add_lesson(
            lesson
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search_patterns(
        self,
        keyword: str
    ):

        return self.memory.learning.find_pattern(
            keyword
        )

    # --------------------------------------------------
    # Insights
    # --------------------------------------------------

    def insights(self):

        return self.memory.learning.summary()

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    def validate(self):

        return True

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.memory.learning.clear()

    def __repr__(self):

        return "<LearningAgent>"


# Singleton
learning_agent = LearningAgent()