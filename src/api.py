import socket
import json


def valid_request(req):
    if not req["method"]:
        return False
    match req["method"]:
        case "GET":
            return True
        case _:
            return False


def read(filters: dict):
    import readers.metro_reader as hr
    reader = hr.MetroDbReader(filters)
    res = []
    for station in reader.read():
        res.append(station)
    return res


def api():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 55882))
    sock.listen(3)

    conn, addr = sock.accept()

    try:
        while True:
            request = json.loads(conn.recv(4096).decode())

            if not request:
                break

            if valid_request(request):
                print(request)
                res = read(request.get("filters", {}))
                json_response = json.dumps({"data": res})
                conn.send(json_response.encode())

    except Exception:
        conn.close()


while True:
    api()
