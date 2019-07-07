"""Electric Appliance Class"""
from inventory_class import Inventory


class ElectricAppliances(Inventory):
    """Electric Appliance Class"""

    def __init__(self, product_code, description, market_price,
                 rental_price, brand, voltage):

        super().__init__(product_code, description, market_price, rental_price)
        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """a method to return a dictionary"""
        output_dict = {}
        super().return_as_dictionary()
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
