import RPi.GPIO as GPIO
from os import system
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

try:
    print("### Shutdown button is enabled. ###")

    def shutdown(channel):
        system("sudo shutdown -h now")

        GPIO.add_event_detect(
            18, GPIO.FALLING, callback=shutdown, bouncetime=100)

        while True:
            pass

# when K/B interrupt occured
except KeyboardInterrupt:
    print("\n### Shutdown button is disabled. ###")
    GPIO.cleanup()
