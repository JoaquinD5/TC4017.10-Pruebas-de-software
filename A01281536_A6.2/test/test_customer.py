"""
Class TestCustomer
Joaquin Diaz    A01281536
"""
import sys
import os
import unittest
from app.customer import Customer  # type: ignore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '..')))


class TestCustomer(unittest.TestCase):
    """
    Unittest for Class Customer.
    """
    def setUp(self):
        """
        SetUp to intialize a Customer instance.
        """
        self.customer = Customer(customer_id="C002",
                                 name="Juan",
                                 email="test@hotmail.com",
                                 cellphone="+5234895623")

    def test_save_obtain_customer(self):
        """
        Test function save_on_file and obtain_customer
        """
        self.customer.save_on_file()
        customer_test_obtain_instance = Customer.obtain_customer(
            customer_id="C002")

        self.assertIsNotNone(customer_test_obtain_instance)
        self.assertEqual(self.customer.customer_id,
                         customer_test_obtain_instance.customer_id)
        self.assertEqual(self.customer.name,
                         customer_test_obtain_instance.name)
        self.assertEqual(self.customer.email,
                         customer_test_obtain_instance.email)
        self.assertEqual(self.customer.cellphone,
                         customer_test_obtain_instance.cellphone)

    def test_load_customers(self):
        """
        Test function load_customers
        """
        self.assertIsNotNone(Customer.load_customers())

    def test_obtain_customer_neg(self):
        """
        Test function obtain_customers with a non existent ID
        """
        customer_test_obtain_instance = Customer.obtain_customer(
            customer_id="C010")
        self.assertIsNone(customer_test_obtain_instance)

    def test_modify_customer(self):
        """
        Test function modify_customer
        """
        customer3 = Customer.obtain_customer(customer_id="C003")
        data = {
            "name": "Jose",
            "email": "test@yahoo.com",
        }
        customer3.modify_customer(new_data=data)
        self.assertEqual(customer3.name, "Jose")
        self.assertEqual(customer3.email, "test@yahoo.com")

    def test_delete_customer(self):
        """
        Test function delete_customer
        """
        Customer.delete_customer(customer_id="C004")
        customer_test_deleted = Customer.obtain_customer(customer_id="C004")
        self.assertIsNone(customer_test_deleted)


if __name__ == '__main__':
    unittest.main()
