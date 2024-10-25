import csv
from models.house import House


class HouseParser:
    """
    class "generator"
    reads file line by line and returns validated House class object
    """
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def _validate(line: [str]) -> House:
        """
        deconstruct line, validate each field
        :param line: string of house data
        :return: valid House object
        """
        try:
            house_id = int(line[0])
        except ValueError:
            house_id = -1
        try:
            latitude = float(line[1].replace(' ', ''))
        except ValueError:
            latitude = -1
        try:
            longitude = float(line[2].replace(' ', ''))
        except ValueError:
            longitude = -1
        try:
            maintenance_year = int(line[3])
        except ValueError:
            maintenance_year = -1
        try:
            square = float(line[4].replace(' ', ''))
        except ValueError:
            square = -1
        try:
            population = int(line[5].replace(' ', ''))
        except ValueError:
            population = -1
        region = line[6]
        locality_name = line[7]
        address = line[8]
        full_address = line[9]
        try:
            communal_service_id = float(line[10].replace(' ', ''))
        except ValueError:
            communal_service_id = -1
        description = line[11]

        return House(
            house_id,
            latitude,
            longitude,
            maintenance_year,
            square,
            population,
            region,
            locality_name,
            address,
            full_address,
            communal_service_id,
            description
        )

    def get_data(self):
        with open(self.filename, "r") as in_f:
            csv_reader = csv.reader(in_f)
            next(csv_reader)  # skip header
            for line in csv_reader:
                yield HouseParser._validate(line)
