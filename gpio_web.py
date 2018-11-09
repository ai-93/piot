from flask import Flask, render_template, redirect, request, jsonify
from gpio_support import get_gpio_list, setup_gpio, toggle_pin
from mqtt_support import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', gpio_list = get_gpio_list())

@app.route('/gpio/<int:pin>')
def gpio_toggle(pin):
    toggle_pin(pin)
    return redirect("/")

if __name__ == '__main__':
    setup_gpio()
    app.run(host="0.0.0.0", port=80)



