#!/usr/bin/python3
"""this module hold unittest for basemodel class"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class."""

    def setUp(self):
        """Set up a new instance of BaseModel for each test."""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Test if BaseModel has the required attributes."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_save(self):
        """Test the functionality of the save method."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertTrue('__class__' in model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.base_model.id)
        self.assertEqual(
                model_dict['created_at'],
                self.base_model.created_at.isoformat()
                )
        self.assertEqual(
                model_dict['updated_at'],
                self.base_model.updated_at.isoformat()
                )

    def test_str(self):
        """Test the string representation of the BaseModel."""
        model_str = str(self.base_model)
        self.assertIsInstance(model_str, str)

    def test_id_generation(self):
        """Test the generation of unique IDs."""
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        base_model = BaseModel(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at
                )
        self.assertEqual(base_model.id, id_val)
        self.assertEqual(base_model.created_at.isoformat(), created_at)
        self.assertEqual(base_model.updated_at.isoformat(), updated_at)

    def test_to_dict_without_datetime_objects(self):
        """Test created_at and updated_at are not datetime objects."""
        base_model = BaseModel()
        base_model.created_at = 'invalid'
        base_model.updated_at = 'invalid'
        model_dict = base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertTrue(isinstance(model_dict['created_at'], str))
        self.assertTrue(isinstance(model_dict['updated_at'], str))

    def test_save_updates_updated_at_only(self):
        """Test that save updates updated_at only."""
        created_at = self.base_model.created_at
        self.base_model.save()
        self.assertEqual(created_at, self.base_model.created_at)

    def test_save_without_storage(self):
        """Test save method when storage is not implemented."""
        self.base_model.save()


if __name__ == '__main__':
    unittest.main()
