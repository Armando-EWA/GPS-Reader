import threading
from gps_reader import GPSReader


# thread = threading.Thread(target=gps_thread)
# thread.start()

if __name__ == '__main__':
    gps = GPSReader(port='COM11', baudrate=4800)
    gps.read()
