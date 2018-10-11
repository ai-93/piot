from flask import Flask, render_template, redirect, request, jsonify
from gpio_support import get_gpio_list, setup_gpio, toggle_pin


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', gpio_list = get_gpio_list())

@app.route('/gpio/<int:pin>')
def gpio_toggle(pin):
    toggle_pin(pin)
    return redirect("/")

if __name__ == '__main__':
    # setup_gpio() todo: uncomment to setup gpio on start
    app.run()



