import sqlite3
import loaders.db_loader as db_loader

"""
functions to upload house object to sqlite
"""


class MetroLoader:

    connection = None

    def __init__(self, metro_records=None):  # metro_records: [[]]

        self.metro_records = metro_records

        # initialize connection on the first execution, reuse in other operations
        if not MetroLoader.connection:
            MetroLoader.connection = sqlite3.connect("data.db")

    def load(self):
        db_loader.load(MetroLoader.connection, "metros", self.metro_records)
