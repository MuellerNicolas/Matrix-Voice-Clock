# Matrix Voice Clock

LED Clock for Matrix Voice Standard and ESP-Version.

Even numbers are represented thorugh 2 shining LEDs, uneven numbers are represented through one shining LED.
Initially the color for the hour hand is blue and the color for the minute hand is red.
If the hands of the watch are crossing the LED is shining in yellow.

The minute hand can be up till 5 minute in advance to the real time. (Clock is never too late compared to the real time)
For e.g. if it's 10:50 realtime, the clock will display 10:50. As soon as it's after 10:50, more specific from 10:51-10:55, the clock will display 10:55. (And so on...)

It's possible to rotate the clock depending on the way your Matrix Voice is placed. (see offset)
You can also adopt the colors.
