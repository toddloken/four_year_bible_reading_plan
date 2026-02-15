"""
 @fileoverview

 Abstract base class for reading plan generation strategies.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from src.models.chapter import Chapter


class BaseStrategy(ABC):
    @abstractmethod
    def generate_plan(self, chapters: List[Chapter], total_days: int) -> Dict:
        pass
