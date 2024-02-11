#!/usr/bin/python3
"""this module test review class"""


import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suite for the Review class."""

    def setUp(self):
        """Set up a new instance of Review for each test."""
        self.review = Review()

    def test_attributes(self):
        """Test if Review has the required attributes."""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_default_values(self):
        """Test the default values of attributes."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        place_id_val = 'test_place_id'
        user_id_val = 'test_user_id'
        text_val = 'test_text'
        review = Review(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
                place_id=place_id_val,
                user_id=user_id_val,
                text=text_val
                )
        self.assertEqual(review.id, id_val)
        self.assertEqual(review.created_at.isoformat(), created_at)
        self.assertEqual(review.updated_at.isoformat(), updated_at)
        self.assertEqual(review.place_id, place_id_val)
        self.assertEqual(review.user_id, user_id_val)
        self.assertEqual(review.text, text_val)

    def test_str(self):
        """Test the string representation of the Review."""
        review_str = str(self.review)
        self.assertIsInstance(review_str, str)


if __name__ == '__main__':
    unittest.main()
