"""
 @fileoverview

 Data model representing a single day's reading assignment.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from dataclasses import dataclass, field
from typing import List
from src.models.chapter import Chapter


@dataclass
class ReadingDay:
    day_number: int
    chapters: List[Chapter] = field(default_factory=list)

    def add_chapter(self, chapter: Chapter) -> None:
        self.chapters.append(chapter)

    @property
    def total_words(self) -> int:
        return sum(ch.word_count for ch in self.chapters)

    @property
    def references(self) -> str:
        from src.services.reference_formatter import ReferenceFormatter
        return ReferenceFormatter.format_references(self.chapters)
