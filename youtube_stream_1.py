#!/usr/bin/env python 
import os 
import time 
import io
import picamera 
import subprocess


YOUTUBE="rtmp://a.rtmp.youtube.com/live2/"		 
KEY= "c8pr-pwxw-bd4g-0dh4" 
#stream_cmd = 'ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY
#stream_cmd = 'ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -vcodec copy -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY


stream_cmd = 'ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/suru-jjfs-4uug-4wk1'				 
#stream_cmd = 'ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i "/home/pi/py_example/video.h264" -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/suru-jjfs-4uug-4wk1'				 

stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
camera = picamera.PiCamera() 
camera.resolution = (640, 480)
#camera.resolution = (1280, 720)  
camera.rotation   = 180	 
camera.crop       = (0.0, 0.0, 1.0, 1.0) 
camera.framerate  = 20 
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

#def stream():
#    print('stream function')
#    camera.wait_recording(1)

	
#def shutdown_pi():
#    print('shutdown pi function') 
#    os.system("sudo shutdown -h now")

#def preview():
#    print('preview  function')
#    stream = io.BytesIO()
#    camera.vflip = True
#    camera.hflip = True
#    camera.capture(stream, use_video_port=True, format='rgb', resize=(320, 240))
#    stream.seek(0)
#    stream.readinto(rgb)
#    stream.close() 

#stream()
#camera.vflip = True 
#camera.hflip = True 
#camera.start_recording(stream_pipe.stdin, format='h264', bitrate = 500000)


camera.wait_recording(1)
print('...start recoding')
#camera.start_recording(stream_pipe.stdin, format='h264', bitrate = 2000000)
camera.start_recording(stream_pipe.stdin, format='h264', bitrate = 500000) 
#camera.start_recording('my_video.h264')
camera.wait_recording(20)
camera.stop_recording()
print('...stop recoding') 