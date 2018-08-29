#!/usr/bin/env python
import os, random

def randomstory ():
	randomfile = random.choice(os.listdir("/home/pi/music/"))
	file = './home/pi/music/'+ randomfile
	os.system("mpg321 + file)
	#os.system ('mplayer' + file)
	#os.system ('omxplayer' + file)

randomstory ()
