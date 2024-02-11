#!/usr/bin/python3
"""module for test case for state"""


import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test suite for the State class."""

    def setUp(self):
        """Set up a new instance of State for each test."""
        self.state = State()

    def test_attributes(self):
        """Test if State has the required attributes."""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_name_attribute(self):
        """Test the name attribute."""
        self.assertEqual(self.state.name, "")

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        name_val = 'test_name'
        state = State(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
                name=name_val
                )
        self.assertEqual(state.id, id_val)
        self.assertEqual(state.created_at.isoformat(), created_at)
        self.assertEqual(state.updated_at.isoformat(), updated_at)
        self.assertEqual(state.name, name_val)

    def test_str(self):
        """Test the string representation of the State."""
        state_str = str(self.state)
        self.assertIsInstance(state_str, str)


if __name__ == '__main__':
    unittest.main()
