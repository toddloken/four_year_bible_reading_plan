"""
 @fileoverview
 *
 ReadingPlan model representing a complete 4-year reading plan.
 *
 @author tjl
 @version 1.0.0
 @since February 2026
"""

from dataclasses import dataclass, field
from typing import List
from src.models.reading_day import ReadingDay


@dataclass
class ReadingPlan:
    name: str
    total_days: int
    reading_days: List[ReadingDay] = field(default_factory=list)

    @property
    def total_words(self) -> int:
        return sum(day.total_words for day in self.reading_days)

    @property
    def average_words_per_day(self) -> float:
        if not self.reading_days:
            return 0.0
        return self.total_words / len(self.reading_days)

    def add_day(self, reading_day: ReadingDay) -> None:
        self.reading_days.append(reading_day)
