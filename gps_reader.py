import serial
import pynmea2
import time
from loguru import logger


class GPSReader:
    def __init__(self, port, baudrate, timeout=1):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.timeout = timeout

    def open_serial(self):
        if not self.ser.is_open:
            try:
                self.ser.open()
                logger.info("Serial port opened.")
            except serial.SerialException as e:
                logger.exception(f"Error opening the serial port: {e}")

    def read(self):
        # Open serial port
        self.open_serial()

        while True:
            # Attempt to reopen if necessary every 5 seconds
            if not self.ser.is_open:
                logger.debug("Serial port is not open. Trying to reopen.")
                time.sleep(5)
                self.open_serial()
                continue  # Skip this iteration

            try:
                line = self.ser.readline().decode('utf-8', errors='replace')
                # logger.info(line)

                if line.startswith('$GNGGA'):
                    # logger.info("line found")

                    try:
                        msg = pynmea2.parse(line)
                        logger.info(msg)

                        lat = msg.latitude if msg.lat_dir == 'N' else str(msg.latitude)
                        lon = msg.longitude if msg.lon_dir == 'E' else str(msg.longitude)
                        logger.info("Latitude Direction: " + msg.lat_dir + " -- Longitude Direction: " + msg.lon_dir)

                        logger.info(f"Latitude: {lat}, Longitude: {lon}")

                    except pynmea2.ParseError as e:
                        logger.exception(e)

                # else:
                #     logger.info("Line not found...")

            except serial.SerialException as e:
                logger.exception(f"Error reading from the serial port: {e}")
                self.ser.close()  # Close the port so it can be reopened next iteration
