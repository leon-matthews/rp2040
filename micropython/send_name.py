import gc
from machine import Pin
import network
import time
import urequests

status_led = Pin("LED", Pin.OUT)
SSID = "rp2-pico"
PASSWORD = "kiwipycon"


def connect():
    # Setup
    status_led.value(0);
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.ifconfig(["192.168.2.118", "255.255.255.0", "192.168.2.1", "1.1.1.1"])
    print(f"Connect to {SSID}")
    wlan.connect(SSID, PASSWORD)
    
    # Wait for connection
    print("Waiting for IP... ", end="")
    while wlan.status() != network.STAT_GOT_IP:
        time.sleep(0.5)
        print(".", end="")
    print("Connected!")
    status_led.value(1);
    

def fetch_data(url):
    """
    Fetch JSON data from given URL.
    
    Returns:
        JSON list or dict
    """
    result = urequests.get(url)
    return result.json()


def post_data(url, data):
    """
    Fetch JSON data from given URL.
    """
    result = urequests.post(url, json=data)
    print(result.status_code)


def main():
    connect()
    data = {
        "text": "Leon 28",
        "color": "#4b8bbe",
    }
    url = "http://192.168.2.2:8000"
    post_data(url, data)
    gc.collect()


if __name__ == '__main__':
    main()
    