import RPi.GPIO as GPIO
import time

#configure
GPIO.setmode(GPIO.BCM)

led_pin = 14# where we plugged it in
GPIO.setup(led_pin, GPIO.OUT)

switch_pin = 23
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# for brightness
#pwm_led = GPIO.PWM(led_pin, 500)
#pwm_led.start(100)

try:
	while True:
		#GPIO.output(led_pin, True) # LED on
		#time.sleep(0.5)
		#GPIO.output(led_pin, False) # LED off
		#time.sleep(0.5)
		
		#duty_s = input("Enter Brightness (0 to 100): ")
		#duty = int(duty_s)
		#pwm_led.ChangeDutyCycle(duty)		
		#GPIO.input(led_pin, True)
		
		if GPIO.input(switch_pin) == False:
			print("Button Pressed")
			GPIO.output(led_pin, True)
			print("Sleeping")
			time.sleep(5)
			GPIO.output(led_pin, False)
		
finally:
	print("cleaning up")
	GPIO.cleanup()