#!/usr/bin/python3
"""Test module for file storage class"""

import unittest
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Test class for file storage"""
    def setUp(self):
        self.storage = FileStorage()
        self.storage.__file_path = "test_file.json"

    def tearDown(self):
        if os.path.exists(self.storage.__file_path):
            os.remove(self.storage.__file_path)

    def test_initialization(self):
        """Test if FileStorage initializes with default attributes"""
        self.assertIsInstance(self.storage.__file_path, str)
        self.assertEqual(self.storage.__file_path, "test_file.json")
        self.assertIsInstance(self.storage.__objects, dict)
        self.assertEqual(len(self.storage.__objects), 0)

    def test_save_and_reload(self):
        """Test if objects are saved and reloaded correctly"""
        obj1 = {'id': '1', 'name': 'Object 1'}
        obj2 = {'id': '2', 'name': 'Object 2'}
        self.storage.__objects['TestObject.1'] = obj1
        self.storage.__objects['TestObject.2'] = obj2
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        self.assertEqual(len(self.storage.__objects), 2)
        self.assertIn('TestObject.1', self.storage.__objects)
        self.assertIn('TestObject.2', self.storage.__objects)
        self.assertEqual(self.storage.__objects['TestObject.1'], obj1)
        self.assertEqual(self.storage.__objects['TestObject.2'], obj2)


if __name__ == '__main__':
    unittest.main()

