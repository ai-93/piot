config = {
    "gpio": [
        {
            "name": "lights",
            "pin": 23,
            "default_state": True,
            "location": "hall"
        },
        {
            "name": "fan",
            "pin": 24,
            "default_state": True,
            "location": "hall"
        }
    ],
    "mqtt": {
        "broker": "m14.cloudmqtt.com",
        "port": 11241,
        "username": "XXXXXXX",
        "password": "XXXXXX"
    }
}
