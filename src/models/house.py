from dataclasses import dataclass


@dataclass
class House:
    """
    struct of house fields
    """
    house_id: int
    latitude: float
    longitude: float
    maintenance_year: int
    square: float
    population: int
    region: str
    locality_name: str
    address: str
    full_address: str
    communal_service_id: float
    description: str
