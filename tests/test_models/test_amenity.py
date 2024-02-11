#!/usr/bin/python3
"""the module test for amenity"""


import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def setUp(self):
        """Set up a new instance of Amenity for each test."""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test if Amenity has the required attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_name_attribute(self):
        """Test the name attribute."""
        self.assertEqual(self.amenity.name, "")

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        name_val = 'test_name'
        amenity = Amenity(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
                name=name_val
                )
        self.assertEqual(amenity.id, id_val)
        self.assertEqual(amenity.created_at.isoformat(), created_at)
        self.assertEqual(amenity.updated_at.isoformat(), updated_at)
        self.assertEqual(amenity.name, name_val)

    def test_str(self):
        """Test the string representation of the Amenity."""
        amenity_str = str(self.amenity)
        self.assertIsInstance(amenity_str, str)


if __name__ == '__main__':
    unittest.main()
