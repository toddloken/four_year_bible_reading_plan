/**
 * @fileoverview
 *
 * Unit tests for DataLoader service.
 *
 * @author tjl
 * @version 1.0.0
 * @since February 2026
 */

import unittest
from pathlib import Path
from src.services.data_loader import DataLoader
from src.config.settings import EXCEL_FILE


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = DataLoader(EXCEL_FILE)

    def test_load_chapters(self):
        chapters = self.loader.load_chapters()
        self.assertGreater(len(chapters), 0)
        self.assertEqual(chapters[0].book, "Genesis")
        self.assertEqual(chapters[0].chapter, 1)

    def test_chapter_attributes(self):
        chapters = self.loader.load_chapters()
        chapter = chapters[0]
        self.assertIsInstance(chapter.book_number, int)
        self.assertIsInstance(chapter.book, str)
        self.assertIsInstance(chapter.chapter, int)
        self.assertIsInstance(chapter.word_count, int)


if __name__ == '__main__':
    unittest.main()
