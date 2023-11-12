from send_data import send
from gpiozero import Button
from signal import pause

attackButton = Button("GPIO4", pull_up=False)
compressorButton = Button("GPIO18", pull_up=False)

compressorButton.when_pressed = send(data={'attackBoolean': 0, 'battery_percentage': 11.2, 'compressorBoolean': 1})


attackButton.is_pressed =  send(data={'attackBoolean': 1, 'compressorBoolean': 0})
compressorButton.is_pressed = send(data={'attackBoolean': 0, 'compressorBoolean': 1})
