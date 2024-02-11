#!/usr/bin/python3
"""module test for city class"""


import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def setUp(self):
        """Set up a new instance of City for each test."""
        self.city = City()

    def test_attributes(self):
        """Test if City has the required attributes."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_default_values(self):
        """Test the default values of attributes."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        state_id_val = 'test_state_id'
        name_val = 'test_name'
        city = City(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
                state_id=state_id_val,
                name=name_val
                )
        self.assertEqual(city.id, id_val)
        self.assertEqual(city.created_at.isoformat(), created_at)
        self.assertEqual(city.updated_at.isoformat(), updated_at)
        self.assertEqual(city.state_id, state_id_val)
        self.assertEqual(city.name, name_val)

    def test_str(self):
        """Test the string representation of the City."""
        city_str = str(self.city)
        self.assertIsInstance(city_str, str)


if __name__ == '__main__':
    unittest.main()
