import time
from datetime import datetime

def real_time_clock():
    try:
        while True:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Clear the console (for a cleaner display)
            print("\033c", end="")
            
            # Display the current time
            print("Current Time:", current_time, end="", flush=True)
            
            # Pause for one second
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nClock stopped.")