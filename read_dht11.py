import time
import Adafruit_DHT
import requests

URL = "http://your_ip"
sensor = Adafruit_DHT.DHT11
pin = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            data = {"temperature": str(t)}
            print(data)
            res = requests.post(URL + "/send-data", data)
        else:
            print("Read Error")

        time.sleep(1)
except KeyboardInterrupt:
    print("Error")

finally:
    print("End Program")
