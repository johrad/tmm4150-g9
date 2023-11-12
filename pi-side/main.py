from time import sleep
import collectData
from send_data import send


from gpiozero import Button
from signal import pause

attackButton = Button("GPIO4", pull_up=False)
compressorButton = Button("GPIO18", pull_up=False)


while True:

    if attackButton.is_pressed:
        send(data={'attackBoolean': 1, 'battery_percentage': 11.2, 'compressorBoolean': 0})
    if compressorButton.is_pressed:
        send(data={'attackBoolean': 0, 'battery_percentage': 11.2, 'compressorBoolean': 1})


    '''
    think loop is easiest, async is pain

    just make a new data setup every x seconds and prevent from adding attackboolean or compressorbolean until x amount of seconds have passed
    
    '''

    sleep(0.2)