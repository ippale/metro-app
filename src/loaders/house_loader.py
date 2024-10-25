import sqlite3
import loaders.db_loader as db_loader

"""
functions to upload house object to sqlite
"""


class HouseLoader:
    """
    IMPORTANT!!! Class accumulates data, after using it, call one more time with no object passed to upload previously accumulated data
    """
    connection = None
    batch_size = 100_000
    house_list = []

    # TODO: commit() method to push not empty buffer to db

    def __init__(self, house_obj=None):  # house_obj: House
        if not house_obj:
            HouseLoader.push_to_db(HouseLoader.house_list)
            return

        self.house_obj = house_obj

        # initialize connection on the first execution, reuse in other operations
        if not HouseLoader.connection:
            HouseLoader.connection = sqlite3.connect("data.db")

    def load(self):
        HouseLoader.house_list.append((self.house_obj.house_id,
                                       self.house_obj.latitude,
                                       self.house_obj.longitude,
                                       self.house_obj.maintenance_year,
                                       self.house_obj.square,
                                       self.house_obj.population,
                                       self.house_obj.region,
                                       self.house_obj.locality_name,
                                       self.house_obj.address,
                                       self.house_obj.full_address,
                                       self.house_obj.communal_service_id,
                                       self.house_obj.description))
        if HouseLoader.batch_size:
            HouseLoader.batch_size -= 1  # decrement batch size
        else:
            HouseLoader.push_to_db(HouseLoader.house_list)
            HouseLoader.house_list = []
            HouseLoader.batch_size = 100

    @staticmethod
    def push_to_db(h_list):
        db_loader.load(HouseLoader.connection, "houses", h_list)
