
from rp2 import bootsel_button
from machine import Pin
import utime


led = Pin("LED", Pin.OUT)


def main():
    previous = False
    while True:
        current = bootsel_button()
        if current and not previous:
            led.toggle()
        previous = current


if __name__ == '__main__':
    main()
