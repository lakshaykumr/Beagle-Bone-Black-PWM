import os
import time

os.system("sudo bash -c \"echo 20000000 > /dev/pwm/ehrpwm1a/period\"")
os.system("sudo bash -c \"echo 10000000 > /dev/pwm/ehrpwm1a/duty_cycle\"")
os.system("sudo bash -c \"echo normal > /dev/pwm/ehrpwm1a/polarity\"")
os.system("sudo bash -c \"echo 1 > /dev/pwm/ehrpwm1a/enable\"")
time.sleep(5)
os.system("sudo bash -c \"echo 0 > /dev/pwm/ehrpwm1a/enable\"")

