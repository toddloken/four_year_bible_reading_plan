"""
 @fileoverview

 Configuration settings for the Bible reading plan generator.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXCEL_FILE = BASE_DIR / 'data' / 'Annual_Reading.xlsx'
OUTPUT_DIR = BASE_DIR / 'output'
OUTPUT_DIR.mkdir(exist_ok=True)
