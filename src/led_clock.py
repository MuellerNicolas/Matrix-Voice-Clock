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
                _adapt_led
        except:
            traceback.print_exc()
        finally:
            pass

    def _adapt_led():
        hour = datetime.now().hour
        minute = datetime.now().minute
        
    def set_minute():
        pass
    
    def set_hour():
        pass