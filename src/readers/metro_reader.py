from dataclasses import dataclass
import sqlite3


@dataclass
class MetroDbReader:
    def __init__(self, filters=None):
        if not filters:
            self.filters = {}
        else:
            self.filters = filters

    def read(self):
        with sqlite3.connect("data.db") as conn:
            cur = conn.cursor()
            clause_query = ''
            for k, v in self.filters.items():
                clause_query = f"{clause_query} and {k} = '{v}'"
            clause_query = f"where 1=1 {clause_query}"
            # print(clause_query)
            select_query = """select * from (
                                select metro_id, metro_name, line_id, line_name, line_hex_color, metro.station_id, station_name, metro.station_lng, metro.station_lat, station_order, houses_num, houses_square, houses_population from
                                metros metro
                                left join metro_stations_aggregated meta
                                on metro.station_id = meta.station_id and metro.station_lng = meta.station_lng and metro.station_lat = meta.station_lat
                                order by metro_id, line_id, metro.station_id)"""
            select_query = f"{select_query} {clause_query}"
            res = cur.execute(select_query).fetchall()
            return res

