"""
Class Hotel
Joaquin Diaz    A01281536
"""

import json
import os


class Hotel:
    """
    Represents a Hotel with basic information and reservation capacity.
    Attributes:
        hotel_id (str): Unique identifier of hotel.
        name (str): Name of hotel.
        location (str): Location of hotel.
        total_rooms (int): Total number of rooms in hotel.
        available_rooms (int): Number of available rooms.
    """

    # File path to save the data
    FILE_PATH = "hoteles.json"

    # Init Hotel
    def __init__(self, hotel_id, data):
        """
        Initialize a new hotel.
        Attributes:
            hotel_id (str): Unique identifier of hotel.
            data (dict): Contains name, location, total_rooms, available_rooms
        """
        self.hotel_id = hotel_id
        self.name = data.get("name", 0)
        self.location = data.get("location", 0)
        self.total_rooms = data.get("total_rooms", 0)
        self.available_rooms = data.get("available_rooms", 0)

    # Save Hotel instance on file
    def save_on_file(self):
        """
        Save hotel instance on file.
        """
        hotels = self.load_hotels()
        if self.hotel_id not in hotels:
            hotels[self.hotel_id] = self.__dict__
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(hotels, file, indent=4)
        else:
            print("Hotel already in file.")

    # Load Hotels
    @classmethod
    def load_hotels(cls):
        """
        Load Hotels
        """
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    # Obtain Hotel information by hotel_id
    @classmethod
    def obtain_hotel(cls, hotel_id):
        """
        Obtain Hotel information by hotel_id
        """
        hotels = cls.load_hotels()
        if hotel_id in hotels:
            data = hotels[hotel_id]
            return Hotel(hotel_id, data)

        print("Hotel not found.")
        return None

    # Delete Hotel information on file by hotel_id
    @classmethod
    def delete_hotel(cls, hotel_id):
        """
        Delete Hotel information on file by hotel_id
        """
        hotels = cls.load_hotels()
        if hotel_id in hotels:
            del hotels[hotel_id]
            with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(hotels, file, indent=4)
        else:
            print("Hotel not found.")

    # Show Information of Hotel
    def display_info(self):
        """
        Show Information of Hotel
        """
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Name of hotel: {self.name}")
        print(f"Hotel location: {self.location}")
        print(f"Available Rooms: {self.available_rooms}/{self.total_rooms}")

    # Modify information of Hotel in file
    def modify_hotel(self, new_data):
        """
        Modify information of Hotel in file
        """
        hotels = self.load_hotels()
        if self.hotel_id in hotels:
            hotels[self.hotel_id].update(new_data)
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(hotels, file, indent=4)
            for key, val in new_data.items():
                if hasattr(self, key):
                    setattr(self, key, val)
        else:
            print("Hotel not found.")

    # Reserve a room
    def reserve_room(self):
        """
        Reserve a room
        """
        if self.available_rooms > 0:
            self.available_rooms -= 1
            self.modify_hotel({"available_rooms": self.available_rooms})
            print("Reservation successful.")
        else:
            print("No available rooms")

    # Cancel Reservation
    def cancel_reservation(self):
        """
        Cancel Reservation
        """
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1
            self.modify_hotel({"available_rooms": self.available_rooms})
            print("Reservation canceled.")
        else:
            print("There is no reservation on file.")
