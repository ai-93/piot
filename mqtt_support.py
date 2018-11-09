from gpio_web import app
from flask_mqtt import Mqtt
from gpio_support import get_gpio_list, setup_gpio, toggle_pin, get_pin_status
from app_config import config

mqtt = Mqtt(app)
app.config['MQTT_BROKER_URL'] = config['mqtt']['broker']
app.config['MQTT_BROKER_PORT'] = config['mqtt']['port']
app.config['MQTT_USERNAME'] = config['mqtt']['username']
app.config['MQTT_PASSWORD'] = config['mqtt']['password']
app.config['MQTT_REFRESH_TIME'] = config['mqtt']['refresh_time']

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    for item in config['gpio']:
        mqtt.subscribe("{}/feeds/{}.{}".format(config['mqtt']['username'], config['location'], item['pin']))


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print (data)
    pin = int(message.topic.split(".")[1])
    state = message.payload.decode()

    if state == "ON":
        state = 0
    else:
        state = 1

    current_state = get_pin_status(pin)
    
    if state != current_state:
        toggle_pin(pin)


def mqtt_publish(pin, value):
    mqtt.publish("{}/feeds/{}.{}".format(config['mqtt']['username'], config['location'], pin), value)
