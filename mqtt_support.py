from gpio_web import app
from flask_mqtt import Mqtt
from gpio_support import toggle_pin, get_pin_status
from config_support import db


app.config['MQTT_BROKER_URL'] = db['mqtt']['broker']
app.config['MQTT_BROKER_PORT'] = db['mqtt']['port']
app.config['MQTT_USERNAME'] = db['mqtt']['username']
app.config['MQTT_PASSWORD'] = db['mqtt']['password']
app.config['MQTT_REFRESH_TIME'] = db['mqtt']['refresh_time']

mqtt = Mqtt(app)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    for item in db['gpio']:
        mqtt.subscribe("{}/feeds/{}.{}".format(db['mqtt']['username'], db['location'], item['pin']))


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
    mqtt.publish("{}/feeds/{}.{}".format(db['mqtt']['username'], db['location'], pin), value)
