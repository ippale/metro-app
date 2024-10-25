import sqlite3


def aggregate():
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        distance_counting_query = """
            insert into metro_stations_meta
            select station_id, station_lat, station_lng, house_id, distance from (
            select station_id, station_lat, station_lng, house_id, latitude, longitude, distance, row_number() over (partition by house_id order by distance) as rn from (
            select h.house_id, h.latitude, h.longitude, m.station_id, m.station_lat, m.station_lng, sqrt(power((h.latitude - m.station_lat)*111.32, 2) + power((h.longitude - m.station_lng)*63, 2)) distance from houses h
                join -- full join
            (select station_id, station_lat, station_lng from metros) m)
            )
            where rn = 1
        """
        cur.execute(distance_counting_query)
        conn.commit()

        aggregation_query = """
            insert into metro_stations_aggregated
            select m.station_id, m.station_lat, m.station_lng, count(h.house_id), sum(h.square), sum(h.population)
                from metro_stations_meta m
            left join
                (select house_id, square, population, address from houses) h
            on m.house_id = h.house_id
            group by m.station_id, m.station_lat, m.station_lng
        """
        cur.execute(aggregation_query)
        conn.commit()

