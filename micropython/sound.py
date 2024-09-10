
from collections import deque

from machine import ADC, Pin
import utime

adc = ADC(Pin(26))


def main():
    history = deque([], 10)
    while True:
        sample = adc.read_u16()
        history.append(sample)
        mean = sum(history) / len(history)
        delta = round(mean - sample)
        bar = abs(40 - delta)
        print("=" * bar)
        utime.sleep(0.1)
    
    
if __name__ == '__main__':
    main()
    