import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


class Write():
    def writeTag(self, data):
        try:
            print("Now place your tag to write")
            reader.write(data)
            print("Written")
        finally:
            GPIO.cleanup()
