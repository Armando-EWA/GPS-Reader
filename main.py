import threading
from gps_reader import GPSReader




# Create and start a new thread running the gps_thread function
# thread = threading.Thread(target=gps_thread)
# thread.start()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gps = GPSReader(port='COM11', baudrate=4800)
    gps.read()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
