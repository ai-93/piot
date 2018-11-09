import RPi.GPIO as GPIO
from config_support import db
from gpio_web import mqtt_publish

def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    for pin_info in db['gpio']:
        GPIO.setup(pin_info['pin'], GPIO.OUT)

        if pin_info['default_state']:
            GPIO.output(pin_info['pin'], 0)
        else:
            GPIO.output(pin_info['pin'], 1)


def toggle_pin(pin):
    status = get_pin_status(pin)
    if status:
        status = "ON"
        GPIO.output(pin, 0)
    else:
        status = "OFF"
        GPIO.output(pin, 1)

    mqtt_publish(pin, status)


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
