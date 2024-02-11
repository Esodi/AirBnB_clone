#!/usr/bin/python3
"""test module for place class"""


import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test suite for the Place class."""

    def setUp(self):
        """Set up a new instance of Place for each test."""
        self.place = Place()

    def test_attributes(self):
        """Test if Place has the required attributes."""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_created_updated_at(self):
        """Test the created_at and updated_at attributes."""
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_default_values(self):
        """Test the default values of attributes."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_kwargs_initialization(self):
        """Test initialization with kwargs."""
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()
        id_val = 'test_id'
        city_id_val = 'test_city_id'
        user_id_val = 'test_user_id'
        name_val = 'test_name'
        description_val = 'test_description'
        number_rooms_val = 3
        number_bathrooms_val = 2
        max_guest_val = 6
        price_by_night_val = 100
        latitude_val = 37.7749
        longitude_val = -122.4194
        amenity_ids_val = ['amenity1', 'amenity2']
        place = Place(
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
                city_id=city_id_val, user_id=user_id_val,
                name=name_val,
                description=description_val,
                number_rooms=number_rooms_val,
                number_bathrooms=number_bathrooms_val,
                max_guest=max_guest_val,
                price_by_night=price_by_night_val,
                latitude=latitude_val,
                longitude=longitude_val,
                amenity_ids=amenity_ids_val
                )
        self.assertEqual(place.id, id_val)
        self.assertEqual(place.created_at.isoformat(), created_at)
        self.assertEqual(place.updated_at.isoformat(), updated_at)
        self.assertEqual(place.city_id, city_id_val)
        self.assertEqual(place.user_id, user_id_val)
        self.assertEqual(place.name, name_val)
        self.assertEqual(place.description, description_val)
        self.assertEqual(place.number_rooms, number_rooms_val)
        self.assertEqual(place.number_bathrooms, number_bathrooms_val)
        self.assertEqual(place.max_guest, max_guest_val)
        self.assertEqual(place.price_by_night, price_by_night_val)
        self.assertEqual(place.latitude, latitude_val)
        self.assertEqual(place.longitude, longitude_val)
        self.assertEqual(place.amenity_ids, amenity_ids_val)

    def test_str(self):
        """Test the string representation of the Place."""
        place_str = str(self.place)
        self.assertIsInstance(place_str, str)


if __name__ == '__main__':
    unittest.main()
