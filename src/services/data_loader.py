"""
 @fileoverview

 Service for loading Bible chapter data from an Excel file.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

import pandas as pd
from pathlib import Path
from typing import List
from src.models.chapter import Chapter


class DataLoader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load_chapters(self) -> List[Chapter]:
        df = pd.read_excel(self.file_path)
        return [
            Chapter(
                book_number=int(row['book_number']),
                book=str(row['book']),
                grouping=int(row['grouping']),
                chapter=int(row['chapter']),
                word_count=int(row['word_count'])
            )
            for _, row in df.iterrows()
        ]
