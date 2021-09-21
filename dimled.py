import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time
#switch = "P9_12"
speed = "P9_14"
#direction ="P9_15"
#GPIO.setup(switch, GPIO.OUT)
#GPIO.setup(direction, GPIO.OUT)

PWM.start(speed, 0)

while True:
        for i in range(0, 100):
                PWM.set_duty_cycle(speed, i)
		#GPIO.output(switch, GPIO.HIGH)
		#GPIO.output(direction, GPIO.HIGH)
		#GPIO.cleanup()
		time.sleep(0.05)
