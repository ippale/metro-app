import json
from models.metro import Metro, MetroLine, MetroStation


class MetroParser:
    """
    class "generator"
    reads file line by line and returns validated Metro class object
    """
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def _get_metro(metro_record) -> Metro:
        """
        read json object and make Metro object
        :param metro_record: single json object contains city metro data
        :return: Metro class object with subclasses structure
        """
        metro_obj = Metro(metro_record["id"], metro_record["name"], [])
        for line in metro_record["lines"]:
            line_obj = MetroLine(line["id"], line["hex_color"], line["name"], [])
            for station in line["stations"]:
                station_obj = MetroStation(station["id"], station["name"], station["lat"], station["lng"],
                                           station["order"])
                line_obj.append(station_obj)
            metro_obj.append(line_obj)
        return metro_obj

    @staticmethod
    def _get_flat_data(metro_obj: Metro) -> [[]]:
        """
        deconstruct Metro class obj to the batch of flat lines (one line for each station)
        :return: list of lists
        """
        res = []
        for line in metro_obj.lines:
            for station in line.stations:
                record = [metro_obj.id,
                          metro_obj.name,
                          metro_obj.url,
                          line.id,
                          line.hex_color,
                          line.name,
                          station.id,
                          station.name,
                          station.lat,
                          station.lng,
                          station.order]
                res.append(record)
        return res

    def get_data(self):
        with open(self.filename, "r") as in_f:
            json_reader = json.load(in_f)
            for obj in json_reader:
                yield MetroParser._get_flat_data(MetroParser._get_metro(obj))
