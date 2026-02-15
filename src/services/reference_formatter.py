"""
 @fileoverview

 Formats chapter lists into compact reference strings.
 Abbreviates book names to 3 letters when references exceed 30 characters.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from typing import List
from src.models.chapter import Chapter

MAX_REF_LENGTH = 30

ABBREVIATIONS = {
    'Genesis': 'Gen', 'Exodus': 'Exo', 'Leviticus': 'Lev',
    'Numbers': 'Num', 'Deuteronomy': 'Deu', 'Joshua': 'Jos',
    'Judges': 'Jdg', 'Ruth': 'Rut', '1 Samuel': '1Sa',
    '2 Samuel': '2Sa', '1 Kings': '1Ki', '2 Kings': '2Ki',
    '1 Chronicles': '1Ch', '2 Chronicles': '2Ch', 'Ezra': 'Ezr',
    'Nehemiah': 'Neh', 'Esther': 'Est', 'Job': 'Job',
    'Psalms': 'Psa', 'Proverbs': 'Pro', 'Ecclesiastes': 'Ecc',
    'Song of Solomon': 'SoS', 'Isaiah': 'Isa', 'Jeremiah': 'Jer',
    'Lamentations': 'Lam', 'Ezekiel': 'Eze', 'Daniel': 'Dan',
    'Hosea': 'Hos', 'Joel': 'Joe', 'Amos': 'Amo',
    'Obadiah': 'Oba', 'Jonah': 'Jon', 'Micah': 'Mic',
    'Nahum': 'Nah', 'Habakkuk': 'Hab', 'Zephaniah': 'Zep',
    'Haggai': 'Hag', 'Zechariah': 'Zec', 'Malachi': 'Mal',
    'Matthew': 'Mat', 'Mark': 'Mar', 'Luke': 'Luk',
    'John': 'Joh', 'Acts': 'Act', 'Romans': 'Rom',
    '1 Corinthians': '1Co', '2 Corinthians': '2Co',
    'Galatians': 'Gal', 'Ephesians': 'Eph', 'Philippians': 'Phi',
    'Colossians': 'Col', '1 Thessalonians': '1Th', '2 Thessalonians': '2Th',
    '1 Timothy': '1Ti', '2 Timothy': '2Ti', 'Titus': 'Tit',
    'Philemon': 'Phm', 'Hebrews': 'Heb', 'James': 'Jam',
    '1 Peter': '1Pe', '2 Peter': '2Pe', '1 John': '1Jo',
    '2 John': '2Jo', '3 John': '3Jo', 'Jude': 'Jud',
    'Revelation': 'Rev'
}


class ReferenceFormatter:
    @staticmethod
    def format_references(chapters: List[Chapter], max_length: int = MAX_REF_LENGTH) -> str:
        if not chapters:
            return ''
        ref = ReferenceFormatter._build_ref_string(chapters, abbreviate=False)
        if max_length == 0 or len(ref) <= max_length:
            return ref
        return ReferenceFormatter._build_ref_string(chapters, abbreviate=True)

    @staticmethod
    def _build_ref_string(chapters: List[Chapter], abbreviate: bool) -> str:
        groups = []
        current_book = None
        start_ch = end_ch = 0

        for ch in chapters:
            if ch.book != current_book:
                if current_book is not None:
                    groups.append((current_book, start_ch, end_ch))
                current_book = ch.book
                start_ch = end_ch = ch.chapter
            elif ch.chapter == end_ch + 1:
                end_ch = ch.chapter
            else:
                groups.append((current_book, start_ch, end_ch))
                start_ch = end_ch = ch.chapter

        if current_book is not None:
            groups.append((current_book, start_ch, end_ch))

        parts = []
        for book, start, end in groups:
            name = ABBREVIATIONS.get(book, book[:3]) if abbreviate else book
            if start == end:
                parts.append(f'{name} {start}')
            else:
                parts.append(f'{name} {start}-{end}')

        return '; '.join(parts)
