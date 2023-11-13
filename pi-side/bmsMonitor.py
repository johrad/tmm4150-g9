from send_data import send
from random import randint
from time import sleep



def bmsMonitor():
    while True:
        # do some sensor reading here
        send(data={'battery_percentage': randint(80,95)})
        sleep(2)