from matrix_lite import led
from time import sleep
from datetime import datetime
import threading
from threading import Lock
from math import ceil

class LEDClock:
    def __init__(self):
        # hour leds
        self._led_array = []
        self._hours_set = False
        # led mapping
        self._switcher = {
            0: self._twelve(),
            1: self._odd(2),
            2: self._even(3),
            3: self._odd(5),
            4: self._even(6),
            5: self._odd(8),
            6: self._even(9),
            7: self._odd(11),
            8: self._even(12),
            9: self._odd(14),
            10: self._even(15),
            11: self._odd(17),
            12: self._twelve()
        }
        # Thread
        self._lock = Lock()
        self._thread_flag = threading.Event()
        self._thread = threading.Thread(target= self._trigger_time, name = 'clock_thread', daemon = True)
        self._thread.start()
    
    def stop_thread(self):
        self._thread_flag.set()
        led.set("black")

    def _trigger_time(self):
        while True:
            # Adapt led every minute
            self._adapt_led()
            sleep(60)

    def _adapt_led(self):
        hour = datetime.now().hour
        minute = datetime.now().minute
        self._set_hour(hour)
        self._hours_set = True
        self._set_minute(minute)
        self._led_array = []
        self._hours_set = False

    def _set_hour(self, hour):
        if hour > 12:
            hour = hour % 12
        print("hour", hour)
        print("after hour")
        print(self._switcher)
        print("")
        led.set(self._switcher[hour])

    def _set_minute(self, minute):
        minute = ceil(minute/5)
        print("minute", minute)
        print("after hour")
        print(self._switcher)
        print("")
        led.set(self._switcher[minute])


    # Methods setting the leds
    def _odd(self, number):
        local_led_array = []
        for x in range(number-2):
            if(not self._hours_set and self._led_array[len(local_led_array)-1] != "blue"):
                self._led_array.append("black")
                local_led_array.append("black")
            local_led_array.append("black")
        if (self._hours_set):
            if(self._led_array[len(local_led_array)-1] == "blue"):
                self._led_array.append("yellow")
                local_led_array.append("yellow")
            else:
                self._led_array.append("red")
                local_led_array.append("red")
        else:
            self._led_array.append("blue")
            local_led_array.append("blue")
        while len(self._led_array) < 18:
            if(not self._hours_set and self._led_array[len(local_led_array)-1] != "blue"):
                self._led_array.append("black")
                local_led_array.append("black")
            local_led_array.append("black")
        return self._led_array
    
    def _even(self, number):
        local_led_array = []
        for x in range(number-2):
            if(not self._hours_set and self._led_array[len(local_led_array)-1] != "blue"):
                self._led_array.append("black")
                local_led_array.append("black")
            local_led_array.append("black")

        if (self._hours_set):
            if(self._led_array[len(local_led_array)-1] == "blue"):
                self._led_array.append("yellow")
                self._led_array.append("yellow")
                local_led_array.append("yellow")
                local_led_array.append("yellow")
            else:
                self._led_array.append("red")
                self._led_array.append("red")
                local_led_array.append("red")
                local_led_array.append("red")
        else:
            self._led_array.append("blue")
            self._led_array.append("blue")
            local_led_array.append("blue")
            local_led_array.append("blue")

        while len(self._led_array) < 18:
            if(not self._hours_set and self._led_array[len(local_led_array)-1] != "blue"):
                self._led_array.append("black")
                local_led_array.append("black")
            local_led_array.append("black")
        return self._led_array

    def _twelve(self):
        local_led_array = []
        if (self._hours_set):
            if(self._led_array[0] == "blue"):
                self._led_array.append("yellow")
                self._led_array.append("yellow")
                local_led_array.append("yellow")
                local_led_array.append("yellow")
            else:
                self._led_array.append("red")
                local_led_array.append("red")
        else:
            self._led_array.append("blue")
            local_led_array.append("blue")
        for x in range(15):
            self._led_array.append("black")
            local_led_array.append("black")
        self._led_array.append("blue")
        local_led_array.append("blue")
        return self._led_array
