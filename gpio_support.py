# import RPi.GPIO as GPIO
from config_support import db
import json

db_dir = "/home/den/piot/db.json"

def toggle_pin(pin):
    status = get_pin_status(pin)

    # GPIO.output(pin, not status)

    update_default_value(pin, status)

def update_default_value(pin, value):
    for pin_info in db['gpio']:
        if pin_info['pin'] == pin:
            pin_info['default_state'] = bool(value)

    with open(db_dir, 'w') as outfile:
        json.dump(db, outfile)


def get_pin_status(pin):
    # status = GPIO.input(pin)
    return True

def get_gpio_list():
    gpio_list = []

    for pin_info in db['gpio']:
        item = {
            "name": pin_info['name'],
            "pin": pin_info['pin'],
            "current_state": get_pin_status(pin_info['pin']),
            "location": pin_info['location']
        }

        gpio_list.append(item)
    
    return gpio_list

def get_location(pin):
    for item in db['gpio']:
        if item['pin'] == pin:
            location = item['location']

    return location