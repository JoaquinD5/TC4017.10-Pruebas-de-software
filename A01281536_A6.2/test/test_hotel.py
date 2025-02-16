"""
Class TestHotel
Joaquin Diaz    A01281536
"""
import sys
import os
import unittest
from app.hotel import Hotel  # type: ignore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestHotel(unittest.TestCase):
    """
    Unittest for Class Hotel.
    """
    def setUp(self):
        """
        SetUp to intialize a Hotel instance.
        """
        hotel_info = {
            "name": "Mariott",
            "location": "Queretaro",
            "total_rooms": 50,
            "available_rooms": 49
        }
        self.hotel = Hotel(hotel_id="H002", data=hotel_info)

    def test_save_obtain_hotel(self):
        """
        Test function save_on_file and obtain_hotel
        """
        self.hotel.save_on_file()
        hotel_test_obtain_instance = Hotel.obtain_hotel(hotel_id="H002")

        self.assertIsNotNone(hotel_test_obtain_instance)
        self.assertEqual(self.hotel.hotel_id,
                         hotel_test_obtain_instance.hotel_id)
        self.assertEqual(self.hotel.name, hotel_test_obtain_instance.name)
        self.assertEqual(self.hotel.location,
                         hotel_test_obtain_instance.location)
        self.assertEqual(self.hotel.total_rooms,
                         hotel_test_obtain_instance.total_rooms)
        self.assertEqual(self.hotel.available_rooms,
                         hotel_test_obtain_instance.available_rooms)

    def test_load_hotels(self):
        """
        Test function load_hotels
        """
        self.assertIsNotNone(Hotel.load_hotels())

    def test_reserve_room(self):
        """
        Test function reserve_room
        """
        hotel1 = Hotel.obtain_hotel(hotel_id="H003")
        rooms_before1 = hotel1.available_rooms
        hotel1.reserve_room()
        self.assertEqual(hotel1.available_rooms, rooms_before1 - 1)

    def test_cancel_reservation(self):
        """
        Test function cancel_reservation
        """
        hotel2 = Hotel.obtain_hotel(hotel_id="H004")
        rooms_before2 = hotel2.available_rooms
        hotel2.cancel_reservation()
        self.assertEqual(hotel2.available_rooms, rooms_before2 + 1)

    def test_modify_hotel(self):
        """
        Test function modify_hotel
        """
        hotel3 = Hotel.obtain_hotel(hotel_id="H005")
        data = {
            "name": "Holiday Inn",
            "location": "Tamaulipas",
        }
        hotel3.modify_hotel(new_data=data)
        self.assertEqual(hotel3.name, "Holiday Inn")
        self.assertEqual(hotel3.location, "Tamaulipas")

    def test_delete_hotel(self):
        """
        Test function delete_hotel
        """
        Hotel.delete_hotel(hotel_id="H006")
        hotel_test_deleted = Hotel.obtain_hotel(hotel_id="H006")
        self.assertIsNone(hotel_test_deleted)


if __name__ == '__main__':
    unittest.main()
