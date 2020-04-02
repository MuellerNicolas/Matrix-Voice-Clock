#from matrix_lite import led
from time import sleep
from led_clock import LEDClock
import traceback

# Testing
#led.set(['red', 'gold', 'purple', {}, 'black', '#6F41C1', 'blue', {'g':255}])
LEDClock = LEDClock(0)
try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    print("Keyboard interrupt!")
except:
    traceback.print_exc()
finally:
    LEDClock.stop_thread()

    

