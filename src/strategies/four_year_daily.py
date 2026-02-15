"""
 @fileoverview

 Daily supplement strategy that distributes remaining chapters (not in monthly
 groupings) plus Psalms and Proverbs across 365 days per year.
 Maintains chronological order while balancing daily word count.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from typing import List, Dict, Set
from src.models.chapter import Chapter
from src.models.reading_day import ReadingDay
from src.strategies.base_strategy import BaseStrategy

WISDOM_BOOKS = {'Psalms', 'Proverbs'}


class FourYearDailyStrategy(BaseStrategy):
    def generate_plan(self, chapters: List[Chapter], grouped_by_year: Dict[int, Set[int]],
                      days: int = 365) -> Dict[int, List[ReadingDay]]:
        wisdom_chapters = [ch for ch in chapters if ch.book in WISDOM_BOOKS]
        wisdom_chapters.sort(key=lambda c: (c.book_number, c.chapter))

        yearly_plans = {}
        for year in range(1, 5):
            excluded = grouped_by_year[year]
            supplement = [ch for ch in chapters
                          if ch.grouping not in excluded and ch.book not in WISDOM_BOOKS]
            supplement.sort(key=lambda c: (c.book_number, c.chapter))
            yearly_plans[year] = self._distribute(supplement, wisdom_chapters, days)

        return yearly_plans

    def _distribute(self, supplement: List[Chapter], wisdom: List[Chapter],
                    days: int) -> List[ReadingDay]:
        psalm_119 = [ch for ch in wisdom if ch.book == 'Psalms' and ch.chapter == 119]
        wisdom_rest = [ch for ch in wisdom if not (ch.book == 'Psalms' and ch.chapter == 119)]

        remaining_days = days - 1
        sup_per_day = self._spread_chapters(supplement, remaining_days)
        wis_per_day = self._spread_chapters(wisdom_rest, remaining_days)

        reading_days = []
        for d in range(remaining_days):
            rd = ReadingDay(day_number=d + 1)
            for ch in sup_per_day[d]:
                rd.add_chapter(ch)
            for ch in wis_per_day[d]:
                rd.add_chapter(ch)
            reading_days.append(rd)

        insert_pos = self._find_psalm_119_position(reading_days)
        p119_day = ReadingDay(day_number=insert_pos + 1)
        for ch in psalm_119:
            p119_day.add_chapter(ch)
        reading_days.insert(insert_pos, p119_day)

        for i, rd in enumerate(reading_days):
            rd.day_number = i + 1

        return reading_days

    @staticmethod
    def _find_psalm_119_position(reading_days: List[ReadingDay]) -> int:
        for i, rd in enumerate(reading_days):
            for ch in rd.chapters:
                if ch.book == 'Psalms' and ch.chapter >= 120:
                    return i
        return len(reading_days)

    @staticmethod
    def _spread_chapters(chapters: List[Chapter], days: int) -> List[List[Chapter]]:
        result = [[] for _ in range(days)]
        if not chapters:
            return result

        total_words = sum(ch.word_count for ch in chapters)
        target = total_words / days
        idx = 0

        for d in range(days):
            while idx < len(chapters):
                ch = chapters[idx]
                current = sum(c.word_count for c in result[d])
                if current == 0 or current + ch.word_count <= target * 1.5:
                    result[d].append(ch)
                    idx += 1
                    if current + ch.word_count >= target * 0.8:
                        break
                else:
                    break
            if idx >= len(chapters):
                break
        return result
