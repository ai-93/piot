from flask import Flask, render_template
from flask_mqtt import Mqtt
from config_support import db
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = db['mqtt']['broker']
app.config['MQTT_BROKER_PORT'] = db['mqtt']['port']
app.config['MQTT_USERNAME'] = db['mqtt']['username']
app.config['MQTT_PASSWORD'] = db['mqtt']['password']
app.config['MQTT_KEEPALIVE'] = 5
mqtt = Mqtt(app)


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
    logging.info(f"{message.topic}")
    logging.info(f"{message.payload.decode()}")

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/tv/state')
# def get_tv_state():
#     tv_state = get_current_tv_state()
#     mqtt.publish("{}/feeds/tv.state".format(db['mqtt']['username']), tv_state)
#     return str(tv_state)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
