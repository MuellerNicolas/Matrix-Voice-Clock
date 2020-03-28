from matrix_lite import led
from time import sleep
from datetime import datetime

class LEDClock:
    def __init__():
        # Thread
        self._lock = Lock()
        self._thread_flag = threading.Event()
        self._thread = threading.Thread(target= self._trigger_time, name = 'clock_thread', daemon = True)
        self._thread.start()
    
    def stop_thread(self):
        self._thread_flag.set()

    def _trigger_time():
        try:
            while True:
                # Adapt led every minute
                sleep(60)
                _adapt_led()
        except:
            traceback.print_exc()
        finally:
            pass

    def _adapt_led():
        hour = datetime.now().hour
        minute = datetime.now().minute
        set_hour(hour)
        set_minute(minute)
        
    def set_hour(hour):
        if hour > 12:
            hour = hour % 12
            switcher = {
                0: twelve(1, 18),
                1: odd(2),
                2: even(3),
                3: odd(5),
                4: even(6),
                5: odd(8),
                6: even(9),
                7: odd(11),
                8: even(12),
                9: odd(14),
                10: even(15),
                11: odd(17),
                12: twelve()
            }
            led.set(switcher.[hour])

        def odd(number):
            led_array = []
            for x in range(number):
                led_array.append("black")
            led_array.append("blue")
            while len(led_array) < 18:
                led_array.append("black")
        
        def even(number):
            led_array = []
            for x in range(number):
                led_array.append("black")
            led_array.append("blue")
            led_array.append("blue")
            while len(led_array) < 18:
                led_array.append("black")

        def twelve():
            led_array = []
            led_array.append("blue")
            for x in range(16):
                led_array.append("black")
            led_array.append("blue")


    def set_minute(minute):
        pass