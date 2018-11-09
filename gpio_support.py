import RPi.GPIO as GPIO
from config_support import db


def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    for pin_info in db['gpio']:
        GPIO.setup(pin_info['pin'], GPIO.OUT)

        GPIO.output(pin_info['pin'], pin_info['default_state'])

def toggle_pin(pin):
    status = get_pin_status(pin)

    GPIO.output(pin, not status)

def get_pin_status(pin):
    status = GPIO.input(pin)
    return status

def get_gpio_list():
    gpio_list = []

    for pin_info in db['gpio']:
        item = {
            "name": pin_info['name'],
            "pin": pin_info['pin'],
            "current_state": get_pin_status(pin_info['pin'])
        }

        gpio_list.append(item)
    
    return gpio_list

def get_location(pin):
    for item in db['gpio']:
        if item['pin'] == pin:
            location = item['location']

    return location