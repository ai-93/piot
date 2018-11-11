# Piot 
> A progressive webapp template.

Web Service for Raspberry pi to control relay connected to it via gpio over a web page, mqtt and google assistant( via [ifttt](https://ifttt.com/))

Flask PWA is supposed to be a goto template when I start a new Flask project. It is constructed on a Model-Template-Controller perspective, which I find clear enough for my current projects.

You can check a live version at [Heroku](https://flask-pwa.herokuapp.com).

## Features

* Blueprint oriented, Flask 1.0 project
* progressive web app
* Service worker based on Workbox

## Installation

```shell
> sudo bash <(wget -qO- https://raw.githubusercontent.com/ai-93/piot/master/setup.sh)
```

# Connection Details (by default piot is configured to work with adafruit mqtt)
You will want to use the following details to connect a MQTT client to [Adafruit IO](https://learn.adafruit.com/adafruit-io/mqtt-api):
```
Host: io.adafruit.com
Port: 1883 or 8883 (for SSL encrypted connection)
Username: your Adafruit account username (see the accounts.adafruit.com page here to find yours)
Password: your Adafruit IO key (click the AIO Key button on a dashboard to find the key)
```


# Google Assistant setup
```
    Create an applet with trigger as google assistant and action as push to adafruit
```


## Usage

### Start/Stop/Restart/Status Server
```shell
> sudo systemctl (start/stop/restart/status) piot
```

## Links

- Repository: https://github.com/ai-93/piot
- Issue tracker: https://github.com/ai-93/piot/issues
- Inspiration and references:
  - [Google's Seu Primeiro PWA](https://developers.google.com/web/fundamentals/codelabs/your-first-pwapp/?hl=pt-br)
  - [Flask PWA demo](https://github.com/uwi-info3180/flask-pwa)
  - [Google's Workbox](https://developers.google.com/web/tools/workbox/)

## Licensing

This project is licensed under MIT license.