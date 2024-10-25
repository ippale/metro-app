import socket
import json
"""
request format = {"method": "GET", "filters": {"field": "value"}}
possible fields: metro_id
                 metro_name 
                 line_id
                 line_name 
                 line_hex_color 
                 station_id
                 station_name 
                 station_lng
                 station_lat 
                 station_order 
                 houses_num 
                 houses_square 
                 houses_population
"""


def format_as_bytes(req: dict):
    return json.dumps(req).encode()


def view(content):

    class MetroViewer:
        def __init__(self, metro_records):
            self.metro_records = metro_records

        def show(self):
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(10, 12))
            # tune parameters
            ax.set_title("MetroMap")
            ax.set_xlabel("longtitude")
            ax.set_ylabel("lattitude")

            lines_set = []
            current_line = []
            current_line_id = self.metro_records[0][2]
            for idx, record in enumerate(self.metro_records):
                if record[2] == current_line_id:
                    current_line.append({"metro_id": record[0],
                                         "metro_name": record[1],
                                         "line_id": record[2],
                                         "line_name": record[3],
                                         "line_hex_color": record[4],
                                         "station_id": record[5],
                                         "station_name": record[6],
                                         "station_lng": record[7],
                                         "station_lat": record[8],
                                         "station_order": record[9],
                                         "houses_num": record[10],
                                         "houses_square": record[11],
                                         "houses_population": record[12]})
                    if idx == len(self.metro_records) - 1:  # pus last line to buffer
                        lines_set.append(current_line)


                else:
                    lines_set.append(current_line)
                    current_line = [{"metro_id": record[0],
                                     "metro_name": record[1],
                                     "line_id": record[2],
                                     "line_name": record[3],
                                     "line_hex_color": record[4],
                                     "station_id": record[5],
                                     "station_name": record[6],
                                     "station_lng": record[7],
                                     "station_lat": record[8],
                                     "station_order": record[9],
                                     "houses_num": record[10],
                                     "houses_square": record[11],
                                     "houses_population": record[12]}]
                    current_line_id = record[2]
            for line in lines_set:
                line_color = f'#{str(line[0]["line_hex_color"]).lower()}'
                lng = [row["station_lng"] for row in line]
                lat = [row["station_lat"] for row in line]
                plt.plot(lng, lat, 'o', linestyle='-', color=line_color)
            plt.show()
    viewer = MetroViewer(content)
    viewer.show()


def main():

    request = {"method": "GET", "filters": {"metro_name": "Москва"}}
    request = format_as_bytes(request)

    sock = socket.socket()
    sock.connect(('0.0.0.0', 55882))
    sock.send(request)
    response = json.loads(sock.recv(655360).decode())
    content = response.get("data", None)
    sock.close()
    if content:
        view(content)


if __name__ == '__main__':
    main()
