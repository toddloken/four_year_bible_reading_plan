"""
 @fileoverview

 Data model representing a monthly reading assignment with grouped chapters.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from dataclasses import dataclass, field
from typing import List
from src.models.chapter import Chapter


@dataclass
class MonthlyReading:
    month_number: int
    month_name: str
    grouping: int
    chapters: List[Chapter] = field(default_factory=list)

    @property
    def total_words(self) -> int:
        return sum(ch.word_count for ch in self.chapters)

    @property
    def book_names(self) -> str:
        seen = []
        for ch in self.chapters:
            if ch.book not in seen:
                seen.append(ch.book)
        return ', '.join(seen)
