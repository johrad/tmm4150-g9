from threading import Thread
from buttonMonitor import buttonMonitor
from bmsMonitor import bmsMonitor

def main():
    # Create threads
    button_thread = Thread(target=buttonMonitor)
    bms_thread = Thread(target=bmsMonitor)

    # Start threads
    button_thread.start()
    bms_thread.start()

    # Wait for threads to finish
    button_thread.join()
    bms_thread.join()

if __name__ == "__main__":
    main()