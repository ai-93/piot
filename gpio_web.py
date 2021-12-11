"""

A small Test application to show how to use Flask-MQTT.

"""

import eventlet
from config_support import db
import json
from flask import Flask, render_template,redirect
import sys
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import logging 
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

eventlet.monkey_patch()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = db['mqtt']['broker']
app.config['MQTT_BROKER_PORT'] = db['mqtt']['port']
app.config['MQTT_USERNAME'] = db['mqtt']['username']
app.config['MQTT_PASSWORD'] = db['mqtt']['password']
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return redirect("http://pi.hole")


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    block = f"{db['mqtt']['username']}/feeds/den.block"
    unblock = f"{db['mqtt']['username']}/feeds/den.unblock"
    logging.info(block)
    logging.info(unblock)
    mqtt.subscribe(block)
    mqtt.subscribe(unblock)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    logging.info(message)
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8081, use_reloader=False, debug=True)
