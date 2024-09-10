
import time

from machine import Pin

led = Pin("LED", Pin.OUT)

def dot():
	led.value(1)
	time.sleep(0.2)
	led.value(0)
	time.sleep(0.3)

def dash():
	led.value(1)
	time.sleep(0.4)
	led.value(0)
	time.sleep(0.3)
	
while True:
	dot(); dot(); dot()
	dash(); dash(); dash()
	dot(); dot(); dot()
	time.sleep(1)
