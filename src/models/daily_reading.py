"""
@fileoverview

DailyReading model for combined monthly grouping and daily supplement readings.

@author tjl
@version 1.0.0
@since February 2026
"""

from dataclasses import dataclass, field
from typing import List
from src.models.chapter import Chapter


@dataclass
class DailyReading:
    day_number: int
    month_name: str
    monthly_grouping: int
    monthly_chapters: List[Chapter] = field(default_factory=list)
    daily_chapters: List[Chapter] = field(default_factory=list)

    @property
    def total_words(self) -> int:
        return (sum(ch.word_count for ch in self.monthly_chapters) +
                sum(ch.word_count for ch in self.daily_chapters))

    @property
    def monthly_references(self) -> str:
        refs = []
        current_book = None
        start_chapter = None
        end_chapter = None
        
        for ch in self.monthly_chapters:
            if current_book != ch.book:
                if current_book:
                    if start_chapter == end_chapter:
                        refs.append(f"{current_book} {start_chapter}")
                    else:
                        refs.append(f"{current_book} {start_chapter}-{end_chapter}")
                current_book = ch.book
                start_chapter = ch.chapter
                end_chapter = ch.chapter
            else:
                end_chapter = ch.chapter
        
        if current_book:
            if start_chapter == end_chapter:
                refs.append(f"{current_book} {start_chapter}")
            else:
                refs.append(f"{current_book} {start_chapter}-{end_chapter}")
        
        return "; ".join(refs) if refs else ""

    @property
    def daily_references(self) -> str:
        refs = []
        for ch in self.daily_chapters:
            refs.append(f"{ch.book} {ch.chapter}")
        return "; ".join(refs) if refs else ""

    @property
    def all_references(self) -> str:
        parts = []
        if self.monthly_references:
            parts.append(f"Monthly: {self.monthly_references}")
        if self.daily_references:
            parts.append(f"Daily: {self.daily_references}")
        return " | ".join(parts)
