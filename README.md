# piot
Web Service for Raspberry pi to control relay connected to it via gpio over a web page, mqtt and google assistant( via [ifttt](https://ifttt.com/))

# Connection Details (by default piot is configured to work with adafruit mqtt)
You will want to use the following details to connect a MQTT client to [Adafruit IO](https://learn.adafruit.com/adafruit-io/mqtt-api):

Host: io.adafruit.com
Port: 1883 or 8883 (for SSL encrypted connection)
Username: your Adafruit account username (see the accounts.adafruit.com page here to find yours)
Password: your Adafruit IO key (click the AIO Key button on a dashboard to find the key)


# Setup
```
    sudo su
    bash <(wget -qO- https://raw.githubusercontent.com/ai-93/piot/master/setup.sh)
```

# Server Status: 
```
    sudo systemctl status piot
```

# Start Server: 
```
    sudo systemctl start piot
```
# Stop Server: 
```
    sudo systemctl stop piot
```

# Google Assistant setup
```
    Create an applet with trigger as google assistant and action as push to adafruit
```
