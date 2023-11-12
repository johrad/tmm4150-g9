from gpiozero import Button
import asyncio
import requests
import send_data
import random as r
from config import serverAddress

# Initialize the battery percentage as a global variable
battery_percentage = 100

def send_sync(data):
    url = f'{serverAddress}/upload'
    response = requests.post(url, json=data)
    print(response.status_code)
    # Add any additional processing of the response if needed

async def send(data):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, send_sync, data)

async def send_battery_percentage():
    while True:
        # Replace this with the actual way you get the battery percentage
        local_battery_percentage = 80
        await send(data={'attackBoolean': 0, 'battery_percentage': local_battery_percentage, 'compressorBoolean': 1})

        # Wait for 2 seconds before sending the next battery percentage
        await asyncio.sleep(2)

async def main():
    global battery_percentage
    attack_button = Button("GPIO4", pull_up=False)
    compressor_button = Button("GPIO18", pull_up=False)

    # Use lambda functions to pass arguments to the when_pressed event
    compressor_button.when_pressed = lambda: send_data.send(data={'attackBoolean': 0, 'battery_percentage': battery_percentage, 'compressorBoolean': 1})
    attack_button.when_pressed = lambda: send_data.send(data={'attackBoolean': 1, 'battery_percentage': battery_percentage, 'compressorBoolean': 0})

    # Start the asynchronous task to send battery percentage
    battery_task = asyncio.create_task(send_battery_percentage())

    # Wait for button events
    await asyncio.gather(
        attack_button.wait_for_press(),
        compressor_button.wait_for_press(),
    )

    # Cancel the battery sending task when button events are done
    battery_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
