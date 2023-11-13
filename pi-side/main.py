from threading import Thread
import time
from buttonMonitor import buttonMonitor
from bmsMonitor import bmsMonitor

def safeButtonMonitor():
    while True:
        try:
            buttonMonitor()
        except Exception as e:
            print(f"buttonMonitor crashed due to {str(e)}. Restarting...")
            time.sleep(1)

def safeBmsMonitor():
    while True:
        try:
            bmsMonitor()
        except Exception as e:
            print(f"bmsMonitor crashed due to {str(e)}. Restarting...")
            time.sleep(1)

def main():
    # Create threads
    button_thread = Thread(target=safeButtonMonitor)
    bms_thread = Thread(target=safeBmsMonitor)

    # Start threads
    button_thread.start()
    bms_thread.start()

    # Wait for threads to finish
    button_thread.join()
    bms_thread.join()

if __name__ == "__main__":
    main()
