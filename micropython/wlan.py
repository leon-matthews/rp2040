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
    wlan.ifconfig(["192.168.2.18", "255.255.255.0", "192.168.2.1", "1.1.1.1"])
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


def main():
    connect()
    ip = fetch_data("http://ip.jsontest.com/")
    print(f"Our IP address is {ip}")
    date = fetch_data("http://date.jsontest.com/")
    print(f"The date is {date}")


if __name__ == '__main__':
    main()
    