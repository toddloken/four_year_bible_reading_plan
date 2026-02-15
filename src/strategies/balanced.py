"""
 @fileoverview
 *
 Balanced reading strategy that distributes chapters evenly by word count.
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


class BalancedStrategy(BaseStrategy):
    def __init__(self, target_words_per_day: int = 600):
        self.target_words_per_day = target_words_per_day

    def generate_plan(self, chapters: List[Chapter], total_days: int) -> ReadingPlan:
        plan = ReadingPlan(name="Balanced Word Count Plan", total_days=total_days)
        
        current_day = ReadingDay(day_number=1)
        day_count = 1

        for chapter in chapters:
            if current_day.total_words + chapter.word_count > self.target_words_per_day and current_day.chapters:
                plan.add_day(current_day)
                day_count += 1
                current_day = ReadingDay(day_number=day_count)
            
            current_day.add_chapter(chapter)

        if current_day.chapters:
            plan.add_day(current_day)

        return plan
