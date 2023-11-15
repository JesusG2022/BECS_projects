from machine import Pin
import utime

trigger = Pin(18, Pin.OUT)
echo = Pin(21, Pin.IN)

def echoTime():
    trigger.value(0)
    utime.sleep_us(5)
    trigger.value(1)
    utime.sleep_us(10)
    trigger.value(0)
    try:
        echoTime = machine.time_pulse_us(echo, 1, 1000000)
        cm = (echoTime * 0.034321) * 0.5
        
        print(str(cm)+" cm")
    except OSError as e:
        print(e)
        
while True:
   echoTime()
   utime.sleep(5)


# Here is the website: https://www.instructables.com/Beginner-Projects-for-Raspberry-Pi-Pico/
# my slide show link: https://docs.google.com/presentation/d/1YkXIeotrGvWZKgX0l3c8hfg1bmvZ65O4xyMUy2L307U/edit?usp=sharing