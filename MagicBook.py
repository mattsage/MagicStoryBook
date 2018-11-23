#Magic Book
from gpiozero import LED, MotionSensor, LightSensor
from signal import pause
ldr = LightSensor(26)
light = LED(25)
def openbook():
	print("Light!")
	led.on()
	os.system("mp321 /home/pi/Twinkle.mp3")	
	randomfile = random.choice(os.listdir("/home/pi/music/"))
	file = '/home/pi/music/'+ randomfile
	#os.system ('omxplayer -o alsa' + file)
	os.system('mp321' + file)
	os.system("mp321 /home/pi/TheEnd.mp3")
def closebook():
	led.off()
	print("Dark!")
	#os.system('killall omxplayer.bin')
	os.system('killall mpg321')
	
ldr.when_light = openbook
ldr.when_dark = closebook
pause()
