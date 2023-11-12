from send_data import send
from gpiozero import Button
from signal import pause

attackButton = Button("GPIO4", pull_up=False)
compressorButton = Button("GPIO18", pull_up=False)

def a():
    print("cock")

attackButton.when_pressed = lambda: send(data={'attackBoolean': 1, 'compressorBoolean': 0})
compressorButton.when_pressed = lambda: send(data={'attackBoolean': 0, 'compressorBoolean': 1})


pause()