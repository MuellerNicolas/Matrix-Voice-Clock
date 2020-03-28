#from matrix_lite import led
from time import sleep
from led_clock import LEDClock

# Testing
#led.set(['red', 'gold', 'purple', {}, 'black', '#6F41C1', 'blue', {'g':255}])
LEDClock = LEDClock()
try:
    while True:
        sleep(10)
except:
    traceback.print_exc()
finally:
    LEDClock.stop_thread()

    

