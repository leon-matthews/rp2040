import time

from machine import ADC


def read_temp():
    """
    Read temperature from internal ADC.
    """
    adc = ADC(ADC.CORE_TEMP)
    voltage = adc.read_u16() * 3.3 / 65_535
    celcius = round(27 - (voltage - 0.706) / 0.001712, 1)
    return celcius


def main():
    while True:
        temp = read_temp()
        print(f"Temperature is {temp}");
        time.sleep(1)


if __name__ == '__main__':
    main()
