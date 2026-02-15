"""
 @fileoverview
 *
 Service for generating reading plans using various strategies.
 *
 @author tjl
 @version 1.0.0
 @since February 2026
"""

from typing import List
from src.models.chapter import Chapter
from src.models.reading_plan import ReadingPlan
from src.strategies.base_strategy import BaseStrategy


class PlanGenerator:
    def __init__(self, strategy: BaseStrategy):
        self.strategy = strategy

    def generate(self, chapters: List[Chapter], total_days: int) -> ReadingPlan:
        return self.strategy.generate_plan(chapters, total_days)

    def set_strategy(self, strategy: BaseStrategy) -> None:
        self.strategy = strategy
