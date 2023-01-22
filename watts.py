from time import sleep

while True:
    with open("/sys/class/power_supply/BAT0/voltage_now") as f:
        volts = int(f.readline()) / 1000000

    with open("/sys/class/power_supply/BAT0/current_now") as f:
        amps = int(f.readline()) / 1000000

    print(f"{volts} voltage | {amps} amps | {volts*amps} watts")
    sleep(1.0)
