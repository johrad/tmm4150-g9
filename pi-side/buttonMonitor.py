from send_data import send
from gpiozero import Button
from time import sleep


def buttonMonitor():
    attackButton = Button("GPIO4", pull_up=False, bounce_time=0.5)
    compressorButton = Button("GPIO18", pull_up=False, bounce_time=0.5)


    while True:
        if attackButton.is_pressed:
            send(data={'attackBoolean': 1, 'compressorBoolean': 0})
            print("attack")
            sleep(1)  # Add a delay to avoid rapid triggering
        elif compressorButton.is_pressed:
            send(data={'attackBoolean': 0, 'compressorBoolean': 1})
            print("cmp")
            sleep(1)  # Add a delay to avoid rapid triggering
        sleep(0.1)