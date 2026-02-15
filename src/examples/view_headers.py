"""
@fileoverview

Example script demonstrating how to access file headers.

@author tjl
@version 1.0.0
@since February 2026
"""

from src.config.settings import EXCEL_FILE
from src.services.data_loader import DataLoader


def main():
    loader = DataLoader(EXCEL_FILE)

    headers = loader.get_headers()

    print("File Header Information")
    print("=" * 50)
    for i, header in enumerate(headers):
        print(f"Column {i}: {header}")
    print("=" * 50)

    chapters = loader.load_chapters()

    print(f"\nFirst 5 chapters loaded:")
    for chapter in chapters[:5]:
        print(f"  {chapter.reference} - {chapter.word_count} words")


if __name__ == "__main__":
    main()
