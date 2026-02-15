"""
 @fileoverview
 *
 Chronological reading strategy that reads chapters in order.
 *
 @author tjl
 @version 1.0.0
 @since February 2026
"""

from typing import List
from src.models.chapter import Chapter
from src.models.reading_day import ReadingDay
from src.models.reading_plan import ReadingPlan
from src.strategies.base_strategy import BaseStrategy


class ChronologicalStrategy(BaseStrategy):
    def __init__(self, chapters_per_day: int = 1):
        self.chapters_per_day = chapters_per_day

    def generate_plan(self, chapters: List[Chapter], total_days: int) -> ReadingPlan:
        plan = ReadingPlan(name="Chronological Reading Plan", total_days=total_days)
        
        for i, chapter in enumerate(chapters):
            day_number = (i // self.chapters_per_day) + 1
            
            if day_number > len(plan.reading_days):
                plan.add_day(ReadingDay(day_number=day_number))
            
            plan.reading_days[-1].add_chapter(chapter)

        return plan
