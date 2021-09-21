import time
import Adafruit_BBIO.PWM as PWM
#PWM.start("P9_16",50)
dtc = input("Enter Duty cycle from 1 to 100:")
PWM.start("P9_16",50)
PWM.set_duty_cycle("P9_16", dtc)
time.sleep(10)
PWM.stop("P9_16")
PWM.cleanup()
