from flask import Flask, render_template, redirect, request, jsonify
from gpio_support import get_gpio_list, setup_gpio, toggle_pin
from mqtt import MqttService

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', gpio_list = get_gpio_list())

@app.route('/gpio/<int:pin>')
def gpio_toggle(pin):
    toggle_pin(pin)
    return redirect("/")

@app.route('/mqtt/push', methods=['POST'])
def mqtt_push():
    content = request.get_json(silent=True)
    mqtt = MqttService()
    print(content)
    
    mqtt.message = content['message']
    mqtt.topic = content['topic']
    
    resp = mqtt.push_once()
    
    return jsonify({"status":200})

if __name__ == '__main__':
    # setup_gpio() todo: uncomment to setup gpio on start
    app.run()



