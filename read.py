import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import requests

reader = SimpleMFRC522()


class Read():
    def readTag():
        
try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()