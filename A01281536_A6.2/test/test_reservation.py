"""
Class TestReservation
Joaquin Diaz    A01281536
"""
import sys
import os
import unittest
from app.reservation import Reservation  # type: ignore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class Testreservation(unittest.TestCase):
    """
    Unittest for Class Reservation.
    """
    def setUp(self):
        """
        SetUp to intialize a Reservation instance.
        """
        self.reservation = Reservation(reservation_id="R002",
                                       customer_id="C004",
                                       hotel_id="H003")

    def test_save_obtain_reservation(self):
        """
        Test function save_on_file and obtain_reservation
        """
        self.reservation.save_on_file()
        reservation_test_obtain_instance = Reservation.obtain_reservation(
            reservation_id="R002")
        self.assertIsNotNone(reservation_test_obtain_instance)
        self.assertEqual(self.reservation.reservation_id,
                         reservation_test_obtain_instance.reservation_id)
        self.assertEqual(self.reservation.customer_id,
                         reservation_test_obtain_instance.customer_id)
        self.assertEqual(self.reservation.hotel_id,
                         reservation_test_obtain_instance.hotel_id)

    def test_load_reservations(self):
        """
        Test function load_reservation
        """
        self.assertIsNotNone(Reservation.load_reservations())

    def test_cancel_reservation(self):
        """
        Test function cancel_reservation
        """
        reservation3 = Reservation.obtain_reservation(reservation_id="R001")
        reservation3.cancel_reservation()
        self.assertEqual(reservation3.state, "canceled")


if __name__ == '__main__':
    unittest.main()
