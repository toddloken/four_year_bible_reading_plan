"""
 @fileoverview

 Data model representing a single Bible chapter with metadata.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from dataclasses import dataclass


@dataclass
class Chapter:
    book_number: int
    book: str
    grouping: int
    chapter: int
    word_count: int
