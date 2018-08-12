#!/usr/bin/env python 
import os 
import time 
import io 
import pygame 
import picamera 
import subprocess 
os.environ['SDL_VIDEODRIVER'] = 'fbcon' 
os.environ['SDL_FBDEV'] = '/dev/fb1' 
os.environ['SDL_MOUSEDEV'] = '/dev/input/touchscreen' 
os.environ['SDL_MOUSEDRV'] = 'TSLIB' 
pygame.init() 
lcd = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
pygame.mouse.set_visible(False) 
img_bg = pygame.image.load('/home/pi/camera_bg.jpg') 
preview_toggle = 0 
stream_toggle = 0 
blue = 26, 0, 255 
white = 255, 255, 255 
cream = 254, 255, 250 
YOUTUBE="rtmp://a.rtmp.youtube.com/live2/"		 
KEY= "c8pr-pwxw-bd4g-0dh4"				 
stream_cmd = 'ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY
stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
camera = picamera.PiCamera() 
camera.resolution = (1080, 720) 
camera.rotation   = 180	 
camera.crop       = (0.0, 0.0, 1.0, 1.0) 
camera.framerate  = 25 
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3) 
def make_button(text, xpo, ypo, color): 
       font=pygame.font.Font(None,24)	 
       label=font.render(str(text),1,(color)) 
       lcd.blit(label,(xpo,ypo)) 
       pygame.draw.rect(lcd, cream, (xpo-5,ypo-5,150,35),1) 
def stream(): 
	camera.wait_recording(1) 
def shutdown_pi(): 
       os.system("sudo shutdown -h now") 
def preview(): 
	stream = io.BytesIO() 
	camera.vflip = True
	camera.hflip = True 
	camera.capture(stream, use_video_port=True, format='rgb', resize=(320, 240)) 
	stream.seek(0) 
	stream.readinto(rgb) 
	stream.close() 
	img = pygame.image.frombuffer(rgb[0:(320 * 240 * 3)], (320, 240), 'RGB') 
	lcd.blit(img, (0,0)) 
	make_button("STOP", 175,200, white) 
	pygame.display.update() 
try: 
	while True: 
		if stream_toggle == 1: 
			stream() 
		elif preview_toggle == 1: 
			preview() 
		else: 
			click_count = 0		 
			lcd.fill(blue) 
			lcd.blit(img_bg,(0,0)) 
			make_button("STREAM", 5, 200, white) 
			make_button("PREVIEW",175,200, white) 
            make_button("POWER", 200, 5, white)
			pygame.display.update() 
		for event in pygame.event.get(): 
			if (event.type == pygame.MOUSEBUTTONDOWN): 
				pos = pygame.mouse.get_pos() 
			if (event.type == pygame.MOUSEBUTTONUP): 
				pos = pygame.mouse.get_pos() 
				print pos 
				x,y = pos 
				if y > 100: 
					if x < 200: 
						print "stream pressed" 
						if stream_toggle == 0 and preview_toggle == 0: 
							stream_toggle = 1 
							lcd.fill(blue) 
							lcd.blit(img_bg,(0,0)) 
							make_button("STOP", 20, 200, white) 
							pygame.display.update() 
							camera.vflip=True 
							camera.hflip = True 
							camera.start_recording(stream_pipe.stdin, format='h264', bitrate = 2000000) 
						elif preview_toggle == 1: 
							preview_toggle = 0 
							lcd.fill(blue) 
							lcd.blit(img_bg,(0,0)) 
							make_button("STREAM", 5, 200, white) 
							make_button("PREVIEW",175,200, white) 
							pygame.display.update() 
						else: 
							stream_toggle = 0 
							lcd.fill(blue) 
							make_button("STREAM", 5, 200, white) 
							make_button("PREVIEW",175,200, white) 
							pygame.display.update() 
							camera.stop_recording() 
					elif x > 225: 
						print "preview pressed" 
						if preview_toggle == 0 and stream_toggle == 0: 
							preview_toggle = 1 
							lcd.fill(blue) 
							make_button("STOP", 175,200, white) 
							pygame.display.update() 
						elif stream_toggle == 1: 
							stream_toggle = 0 
							lcd.fill(blue) 
							make_button("STREAM", 5, 200, white) 
							make_button("PREVIEW",175,200, white) 
							pygame.display.update() 
							camera.stop_recording() 
						else: 
							preview_toggle = 0 
							lcd.fill(blue) 
							make_button("STREAM", 5, 200, white) 
							make_button("PREVIEW",175,200, white) 
							pygame.display.update() 
except KeyboardInterrupt: 
	camera.stop_recording() 
	print ' Exit Key Pressed' 
finally: 
	camera.close() 
	stream_pipe.stdin.close() 
	stream_pipe.wait() 
	print("Camera safely shut down") 
	print("Good bye") 