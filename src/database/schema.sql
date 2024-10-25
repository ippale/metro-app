CREATE TABLE IF NOT EXISTS houses (
    house_id int primary key,
    latitude float,
    longitude float,
    maintenance_year int,
    square float,
    population int,
    region text,
    locality_name text,
    address text,
    full_address text,
    communal_service_id float,
    description text
);
CREATE TABLE IF NOT EXISTS metros (
    metro_id int,
    metro_name text,
    metro_url text,
    line_id int,
    line_hex_color text,
    line_name text,
    station_id float,
    station_name text,
    station_lat float,
    station_lng float,
    station_order int
);
CREATE TABLE IF NOT EXISTS metro_stations_aggregated(
  station_id float,
  station_lat float,
  station_lng float,
  houses_num int,
  houses_square float,
  houses_population int
);
CREATE TABLE IF NOT EXISTS metro_stations_meta(
  station_id float,
  station_lat float,
  station_lng float,
  house_id INT,
  distance float
);
