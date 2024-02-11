#!/usr/bin/python3
""" Test module for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test class for base model class"""
    def test_default_attributes(self):
        """Test if BaseModel initializes with default attributes"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_custom_attributes(self):
        """Test if BaseModel initializes with custom attributes"""
        custom_id = str(uuid.uuid4())
        custom_created_at = datetime.now()
        custom_updated_at = datetime.now()

        obj = BaseModel(
            id=custom_id,
            created_at=custom_created_at,
            updated_at=custom_updated_at
        )
        self.assertEqual(obj.id, custom_id)
        self.assertEqual(obj.created_at, custom_created_at)
        self.assertEqual(obj.updated_at, custom_updated_at)

    def test_str_representation(self):
        """Test if BaseModel returns a proper string representation"""
        obj = BaseModel()
        expected_string = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_string)

    def test_save_method(self):
        """Test if save method updates the updated_at attribute"""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, prev_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns the expected dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at)
        self.assertEqual(obj_dict['updated_at'], obj.updated_at)


if __name__ == '__main__':
    unittest.main()
