import gc
from machine import Pin
import network
import struct
import utime

from umqtt.simple import MQTTClient
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
        utime.sleep(0.5)
        print(".", end="")
    print("Connected!")
    status_led.value(1);
    

def mqtt_send():
    broker = "192.168.2.2"
    client_id = f"Leon18"
    topic = b"grid/18"
    client = MQTTClient(client_id, broker)
    client.connect()
    message = create_message()
    print(message)
    client.publish(topic, message)
    client.disconnect()
    

def create_message():
    # Build message
    text = "Leon "
    text_length = len(text)
    color = (75, 139, 190)
    value = 320
    msb = value >> 8 & 0xff
    lsb = value & 0xff
    data = (
        bytearray([text_length]) +
        text.encode('utf-8') +
        bytearray(color) +
        bytearray((msb, lsb))
    )
    return data
    

def main():
    connect()
    mqtt_send()
    gc.collect()


if __name__ == '__main__':
    main()
    