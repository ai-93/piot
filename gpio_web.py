from flask import Flask, render_template, redirect, request, jsonify
from gpio_support import get_gpio_list, setup_gpio, get_pin_status, toggle_pin, get_location
from flask_mqtt import Mqtt
from config_support import db
from support import get_current_tv_state
import requests

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = db['mqtt']['broker']
app.config['MQTT_BROKER_PORT'] = db['mqtt']['port']
app.config['MQTT_USERNAME'] = db['mqtt']['username']
app.config['MQTT_PASSWORD'] = db['mqtt']['password']
app.config['MQTT_REFRESH_TIME'] = db['mqtt']['refresh_time']
mqtt = Mqtt(app)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe("{}/feeds/tv.state".format(db['mqtt']['username']))
    for item in db['gpio']:
        mqtt.subscribe("{}/feeds/{}.{}".format(db['mqtt']['username'], item['location'], item['pin']))

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
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
    location = get_location(pin)
    mqtt.publish("{}/feeds/{}.{}".format(db['mqtt']['username'], location, pin), value)


@app.route('/')
def main():
    return render_template('index.html', gpio_list = get_gpio_list(), tv_state = get_current_tv_state())

@app.route('/gpio/<int:pin>')
def gpio_toggle(pin):
    toggle_pin(pin)

    current_state = get_pin_status(pin)

    if current_state:
        status = "OFF"
    else:
        status = "ON"

    mqtt_publish(pin, status)
    return redirect("/")

@app.route('/ir/tv/<int:state>')
def tv_ir_toggle(state):
    if(state == 1):
        requests.get("https://maker.ifttt.com/trigger/tv_on/with/key/c7gXS9qsxTuTtG2n5OZaY3")
    else:
        requests.get("https://maker.ifttt.com/trigger/tv_off/with/key/c7gXS9qsxTuTtG2n5OZaY3")
    
    return redirect("/")

@app.route('/ir/ac/<int:state>')
def ac_ir_toggle(state):
    if(state == 1):
        requests.get("https://maker.ifttt.com/trigger/ac_on/with/key/c7gXS9qsxTuTtG2n5OZaY3")
    else:
        requests.get("https://maker.ifttt.com/trigger/ac_off/with/key/c7gXS9qsxTuTtG2n5OZaY3")
    
    return redirect("/")


@app.route('/tv/state')
def get_tv_state():
    tv_state = get_current_tv_state()
    mqtt.publish("{}/feeds/tv.state".format(db['mqtt']['username']), tv_state)
    return str(tv_state)

if __name__ == '__main__':
    setup_gpio()
    app.run(host="0.0.0.0", port=8080, debug=True)
