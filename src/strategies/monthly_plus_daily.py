"""
@fileoverview

Strategy that combines monthly book groupings with daily Psalms/Proverbs readings.
Creates a 365-day plan where each day includes chapters from the current month's
grouping plus daily portions of Psalms and Proverbs.

@author tjl
@version 1.0.0
@since February 2026
"""

import random
from typing import List, Dict, Set
from datetime import date, timedelta
from src.models.chapter import Chapter
from src.models.daily_reading import DailyReading
from src.strategies.base_strategy import BaseStrategy


class MonthlyPlusDailyStrategy(BaseStrategy):
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def __init__(self, daily_books: Set[str] = None, seed: int = None, year: int = 2026):
        self.gospel_assignments = {'Matthew': 1, 'Mark': 2, 'Luke': 3, 'John': 4}
        #self.daily_books = daily_books or {'Psalms', 'Proverbs'}
        self.daily_books = daily_books or {'Psalms', 'Proverbs'}
        self.seed = seed
        self.year = year
        if seed is not None:
            random.seed(seed)

    def generate_plan(self, chapters: List[Chapter], total_days: int) -> Dict[int, List[DailyReading]]:
        monthly_grouping_chapters = {1: [], 2: [], 3: [], 4: []}
        daily_chapters = []
        remaining_groupings = {}
        
        for chapter in chapters:
            if chapter.book in self.daily_books:
                daily_chapters.append(chapter)
            elif chapter.book in self.gospel_assignments:
                year = self.gospel_assignments[chapter.book]
                monthly_grouping_chapters[year].append(chapter)
            else:
                if chapter.grouping not in remaining_groupings:
                    remaining_groupings[chapter.grouping] = []
                remaining_groupings[chapter.grouping].append(chapter)
        
        groupings_per_year = {}
        for year in range(1, 5):
            unique_groupings = set(ch.grouping for ch in monthly_grouping_chapters[year])
            groupings_per_year[year] = len(unique_groupings)
        
        grouping_list = list(remaining_groupings.keys())
        random.shuffle(grouping_list)
        
        target_per_year = 12
        for grouping in grouping_list:
            year = min(groupings_per_year, key=groupings_per_year.get)
            
            if groupings_per_year[year] < target_per_year:
                monthly_grouping_chapters[year].extend(remaining_groupings[grouping])
                groupings_per_year[year] += 1
        
        for year in range(1, 5):
            monthly_grouping_chapters[year].sort(key=lambda ch: (ch.grouping, ch.book_number, ch.chapter))
        
        daily_chapters.sort(key=lambda ch: (ch.book_number, ch.chapter))
        
        yearly_plans = {}
        for year_num in range(1, 5):
            yearly_plans[year_num] = self._create_daily_schedule(
                year_num, 
                monthly_grouping_chapters[year_num],
                daily_chapters
            )
        
        return yearly_plans

    def _create_daily_schedule(self, year_num: int, monthly_chapters: List[Chapter], 
                               daily_chapters: List[Chapter]) -> List[DailyReading]:
        grouping_dict = {}
        for ch in monthly_chapters:
            if ch.grouping not in grouping_dict:
                grouping_dict[ch.grouping] = []
            grouping_dict[ch.grouping].append(ch)
        
        sorted_groupings = sorted(grouping_dict.keys())[:12]
        
        month_assignments = []
        for i, grouping in enumerate(sorted_groupings):
            month_assignments.append({
                'month_index': i,
                'month_name': self.MONTHS[i],
                'grouping': grouping,
                'chapters': grouping_dict[grouping],
                'days_in_month': self.DAYS_PER_MONTH[i]
            })
        
        daily_per_day = len(daily_chapters) / 365.0
        
        daily_readings = []
        day_counter = 1
        daily_chapter_index = 0
        
        for month_info in month_assignments:
            chapters_this_month = month_info['chapters']
            days_in_month = month_info['days_in_month']
            
            chapters_per_day = len(chapters_this_month) / days_in_month
            monthly_chapter_index = 0
            
            for day_in_month in range(days_in_month):
                daily_reading = DailyReading(
                    day_number=day_counter,
                    month_name=month_info['month_name'],
                    monthly_grouping=month_info['grouping']
                )
                
                monthly_chapters_for_day = int((day_in_month + 1) * chapters_per_day) - int(day_in_month * chapters_per_day)
                for _ in range(monthly_chapters_for_day):
                    if monthly_chapter_index < len(chapters_this_month):
                        daily_reading.monthly_chapters.append(chapters_this_month[monthly_chapter_index])
                        monthly_chapter_index += 1
                
                daily_chapters_for_day = int((day_counter) * daily_per_day) - int((day_counter - 1) * daily_per_day)
                for _ in range(daily_chapters_for_day):
                    if daily_chapter_index < len(daily_chapters):
                        daily_reading.daily_chapters.append(daily_chapters[daily_chapter_index])
                        daily_chapter_index += 1
                
                daily_readings.append(daily_reading)
                day_counter += 1
        
        return daily_readings

    def _get_book_display_name(self, grouping: int, chapters: List[Chapter]) -> str:
        if grouping == 18:
            return "Isaiah 1-33"
        elif grouping == 19:
            return "Isaiah 34-66"
        else:
            unique_books = []
            seen = set()
            for chapter in chapters:
                if chapter.book not in seen:
                    unique_books.append(chapter.book)
                    seen.add(chapter.book)
            return ', '.join(unique_books)
