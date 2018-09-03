#MagicalBook.py
import time import sleep
import os
from gpiozero import LED, LightSensor

ldr = LightSensor(18, queue_len=1)
led = LED(25)
led.off()
while True:

	if ldr.wait_for_light()
		print("Light!")
		led.on()
		randomfile = random.choice(os.listdir("/home/pi/music/"))
		file = '/home/pi/music/'+ randomfile
		#os.system ('omxplayer' + file)
		os.system('mp321' + file)

	#time.sleep(5)


	if ldr.wait_for_dark()
		led.off()
		print("Dark!")
		#ldr.when_dark()
		#os.system('killall omxplayer.bin')
		os.system('killall mpg321')
	sleep(0.2)
