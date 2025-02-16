"""
Class Reservation
Joaquin Diaz    A01281536
"""

import json
import os


class Reservation:
    """
    Represents a reservation.
    Attributes:
        reservation_id (str): Unique identifier of reservation.
        customer_id (str): Customer identifier who made the reservation.
        hotel_id (str): Hotel identifier where reservation was made.
        state (str): State of the reservation, active or canceled.
    """

    # File path to save the data
    FILE_PATH = "reservation.json"

    # Init reservation
    def __init__(self, reservation_id, customer_id, hotel_id, state="active"):
        """
        Initialize a new reservation.

        Attributes:
            reservation_id (str): Unique identifier of reservation.
            customer_id (str): Customer identifier who made the reservation.
            hotel_id (str): Hotel identifier where reservation was made.
            state (str): State of the reservation, active or canceled.
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.state = state

    # Save Reservation instance on file
    def save_on_file(self):
        """
        Save reservation instance on file.
        """
        reservations = self.load_reservations()
        if self.reservation_id not in reservations:
            reservations[self.reservation_id] = self.__dict__
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(reservations, file, indent=4)
        else:
            print("Reservation id already on file.")

    # Load Reservations
    @classmethod
    def load_reservations(cls):
        """
        Load reservations.
        """
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    # Obtain Reservation information by reservation_id
    @classmethod
    def obtain_reservation(cls, reservation_id):
        """
        Obtain reservation information by reservation_id
        """
        reservations = cls.load_reservations()
        if reservation_id in reservations:
            data = reservations[reservation_id]
            return Reservation(**data)
        print("Customer not found.")
        return None

    # Cancel Reservation information on file by reservation_id
    def cancel_reservation(self):
        """
        Cancel reservation information on file by reservation_id
        """
        reservations = self.load_reservations()
        if self.reservation_id in reservations:
            reservations[self.reservation_id].update({"state": "canceled"})
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(reservations, file, indent=4)
            if hasattr(self, "state"):
                setattr(self, "state", "canceled")
        else:
            print("Reservation not found.")
