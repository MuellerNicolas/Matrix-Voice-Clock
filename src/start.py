from time import sleep
from led_clock import LEDClock
import traceback

# set the offset of led (to the right)
# set the colors for hour, minute and for hour and minute crossing
LEDClock = LEDClock(0, "blue", "red", "yellow")
LEDClock.display_time()
try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    print("Keyboard interrupt!")
except:
    traceback.print_exc()
finally:
    LEDClock.stop_thread()

    

