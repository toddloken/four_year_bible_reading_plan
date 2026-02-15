"""
 @fileoverview

 Four-year grouping strategy that distributes Bible groupings across 4 years.
 Each year has 12 months with one grouping per month.
 Gospels are assigned to specific years; remaining groupings are randomized.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

import random
from typing import List, Dict, Set
from src.models.chapter import Chapter
from src.models.monthly_reading import MonthlyReading
from src.strategies.base_strategy import BaseStrategy

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

GOSPEL_ASSIGNMENTS = {'Matthew': 1, 'Mark': 2, 'Luke': 3, 'John': 4}
EXCLUDED_BOOKS = {'Psalms', 'Proverbs'}


class FourYearGroupingStrategy(BaseStrategy):
    def __init__(self, seed: int = None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def generate_plan(self, chapters: List[Chapter], total_days: int) -> Dict[int, List[MonthlyReading]]:
        grouped_chapters = {y: [] for y in range(1, 5)}
        remaining_groupings = {}

        for ch in chapters:
            if ch.book in EXCLUDED_BOOKS:
                continue
            if ch.book in GOSPEL_ASSIGNMENTS:
                grouped_chapters[GOSPEL_ASSIGNMENTS[ch.book]].append(ch)
            else:
                remaining_groupings.setdefault(ch.grouping, []).append(ch)

        groupings_per_year = {
            y: len(set(ch.grouping for ch in grouped_chapters[y])) for y in range(1, 5)
        }

        grouping_list = list(remaining_groupings.keys())
        random.shuffle(grouping_list)

        for grouping in grouping_list:
            year = min(groupings_per_year, key=groupings_per_year.get)
            if groupings_per_year[year] < 12:
                grouped_chapters[year].extend(remaining_groupings[grouping])
                groupings_per_year[year] += 1

        yearly_plans = {}
        for year in range(1, 5):
            grouped_chapters[year].sort(key=lambda c: (c.grouping, c.book_number, c.chapter))
            grouping_dict = {}
            for ch in grouped_chapters[year]:
                grouping_dict.setdefault(ch.grouping, []).append(ch)

            sorted_groupings = sorted(grouping_dict.keys())
            yearly_plans[year] = [
                MonthlyReading(
                    month_number=i + 1,
                    month_name=MONTHS[i] if i < 12 else f'Month {i + 1}',
                    grouping=g,
                    chapters=grouping_dict[g]
                )
                for i, g in enumerate(sorted_groupings)
            ]

        return yearly_plans
