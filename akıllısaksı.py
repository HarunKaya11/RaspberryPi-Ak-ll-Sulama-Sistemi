import time
import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



role=22
buzzer_pin=27
mavi_led=26
kirmizi_led=17

GPIO.setup(role, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(kirmizi_led, GPIO.OUT)
GPIO.setup(mavi_led, GPIO.OUT)



def Buzzer(buzzer_pin):
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer_pin, GPIO.LOW)
    
def kırmızı(led1):
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led1, GPIO.LOW)
    
def mavi(led2):
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led2, GPIO.LOW)

def get_moisture(pin = 4):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)


    
def pump(röle_pin):
	GPIO.output(röle_pin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(röle_pin, GPIO.HIGH)
	return
	

while True:
    if get_moisture(pin = 4) == 1:
	    pump(role)
	    Buzzer(buzzer_pin)
	    kırmızı(kirmizi_led)
    if get_moisture(pin= 4) == 0:
	    mavi(mavi_led)
	
		
			
	
	

