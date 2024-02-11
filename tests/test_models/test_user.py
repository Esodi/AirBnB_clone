#!/usr/bin/python3
"""test module for user class"""


import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test suite for the User class."""

    def setUp(self):
        """Set up a new instance of User for each test."""
        self.user = User()

    def test_attributes(self):
        """Test if User has the required attributes."""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_email_attribute(self):
        """Test the email attribute."""
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test the password attribute."""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test the first_name attribute."""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test the last_name attribute."""
        self.assertEqual(self.user.last_name, "")

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        email_val = 'test_email'
        password_val = 'test_password'
        first_name_val = 'test_first_name'
        last_name_val = 'test_last_name'
        user = User(id=id_val, created_at=created_at, updated_at=updated_at,
                    email=email_val, password=password_val,
                    first_name=first_name_val, last_name=last_name_val)
        self.assertEqual(user.id, id_val)
        self.assertEqual(user.created_at.isoformat(), created_at)
        self.assertEqual(user.updated_at.isoformat(), updated_at)
        self.assertEqual(user.email, email_val)
        self.assertEqual(user.password, password_val)
        self.assertEqual(user.first_name, first_name_val)
        self.assertEqual(user.last_name, last_name_val)

    def test_str(self):
        """Test the string representation of the User."""
        user_str = str(self.user)
        self.assertIsInstance(user_str, str)


if __name__ == '__main__':
    unittest.main()
