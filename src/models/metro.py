from dataclasses import dataclass


@dataclass
class MetroStation:
    id: float
    name: str
    lat: float
    lng: float
    order: int


@dataclass
class MetroLine:
    id: int
    hex_color: str
    name: str
    stations: [MetroStation]

    def append(self, station: MetroStation):
        self.stations.append(station)


@dataclass
class Metro:
    id: int
    name: str
    lines: [MetroLine]
    url: str = ''

    def append(self, line: MetroLine):
        self.lines.append(line)
