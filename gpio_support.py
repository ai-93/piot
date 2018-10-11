# import RPi.GPIO as GPIO
from app_config import config

def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    for pin_info in config['gpio']:
        GPIO.setup(pin_info['pin'], GPIO.OUT)

        if pin_info['default_state']:
            GPIO.output(pin_info['pin'], 0)
        else:
            GPIO.output(pin_info['pin'], 1)


def toggle_pin(pin):  # todo: change to actual toggle function
    status = get_pin_status(pin)
    # if status:
    #     GPIO.output(pin_info['pin'], 0)
    # else:
    #     GPIO.output(pin_info['pin'], 1)
    print (status)
    print (pin)


def get_pin_status(pin):
    # status = GPIO.input(pin)
    # print status
    return True # todo: change to actual value


def get_gpio_list():
    gpio_list = []

    for pin_info in config['gpio']:
        item = {
            "name": pin_info['name'],
            "pin": pin_info['pin'],
            "current_state": get_pin_status(pin_info['pin'])
        }

        gpio_list.append(item)
    
    return gpio_list
