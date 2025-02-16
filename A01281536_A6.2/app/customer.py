"""
Class Customer
Joaquin Diaz    A01281536
"""

import json
import os


class Customer:
    """
    Represents a Customer with basic information.
    Attributes:
        customer_id (str): Unique identifier of Customer.
        name (str): Name of Customer.
        email (str): Email of Customer.
        cellphone (str): Cellphone of Customer.
    """

    # File path to save the data
    FILE_PATH = "customer.json"

    # Init Customer
    def __init__(self, customer_id, name, email, cellphone):
        """
        Initialize a new customer.

        Attributes:
            customer_id (str): Unique identifier of customer.
            name (str): Name of Customer.
            email (str): Email of Customer.
            cellphone (str): Cellphone of Customer.
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cellphone = cellphone

    # Save Customer instance on file
    def save_on_file(self):
        """
        Save customer instance on file.
        """
        customers = self.load_customers()
        if self.customer_id not in customers:
            customers[self.customer_id] = self.__dict__
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(customers, file, indent=4)
        else:
            print("Customer id already on file.")

    # Load Customers
    @classmethod
    def load_customers(cls):
        """
        Load Customers.
        """
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    # Obtain Customer information by customer_id
    @classmethod
    def obtain_customer(cls, customer_id):
        """
        Obtain Customer information by customer_id
        """
        customers = cls.load_customers()
        if customer_id in customers:
            data = customers[customer_id]
            return Customer(**data)

        print("Customer not found.")
        return None

    # Delete Customer information on file by customer_id
    @classmethod
    def delete_customer(cls, customer_id):
        """
        Delete Customer information on file by customer_id
        """
        customers = cls.load_customers()
        if customer_id in customers:
            del customers[customer_id]
            with open(cls.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(customers, file, indent=4)
        else:
            print("Customer not found.")

    # Show information of Customer
    def display_info(self):
        """
        Show information of Customer
        """
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Cellphone: {self.cellphone}")

    # Modify information of Customer in file
    def modify_customer(self, new_data):
        """
        Modify information of Customer in file
        """
        customers = self.load_customers()
        if self.customer_id in customers:
            customers[self.customer_id].update(new_data)
            with open(self.FILE_PATH, "w", encoding="utf-8") as file:
                json.dump(customers, file, indent=4)
            for key, val in new_data.items():
                if hasattr(self, key):
                    setattr(self, key, val)
        else:
            print("customer not found.")
