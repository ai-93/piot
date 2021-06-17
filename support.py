import requests

def get_current_tv_state():
    try:
        response = requests.get("http://192.168.1.25:4004",timeout=5)
        if response.status_code == 400:
            response = True
        else:
            response = False
    except:
        response = False
    
    return response