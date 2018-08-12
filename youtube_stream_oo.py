#!/usr/bin/env python
import os
import time
import io
import picamera
import subprocess


YOUTUBE="rtmp://a.rtmp.youtube.com/live2/"
#KEY= "abdq-sv6g-5a1m-2d72"
#stream_cmd = 'ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY
#stream_cmd = 'ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -vcodec copy -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY
#stream_cmd = 'ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i "/home/pi/py_example/video.h264" -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/suru-jjfs-4uug-4wk1'



#stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE)
#camera = picamera.PiCamera()
#camera.resolution = (640, 480)
#camera.resolution = (1280, 720)
#camera.rotation   = 0
#camera.crop       = (0.0, 0.0, 1.0, 1.0)
#camera.framerate  = 30
#rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3)

#recording video parameter for 640x480
#r_bitrate = 500000 #recording bitrate
#r_time = 60*60*3  #recording time


class YouTube_Stream():
    def __init__(self,key):
       	#
        YOUTUBE_KEY = key
        stream_cmd = 'ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv ' + YOUTUBE + YOUTUBE_KEY
        self.stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE)
        print('>> init Youtube')
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        #camera.resolution = (1280, 720)
        self.camera.rotation   = 0
        #camera.crop       = (0.0, 0.0, 1.0, 1.0)
        self.camera.framerate  = 30
        rgb = bytearray(self.camera.resolution[0] * self.camera.resolution[1] * 3)
        #

    def start_Youtube_Stream(self,r_bitrate=0,r_time=0):
        print('>> Start Youtube Sreaming')
        print('set bitrate=' + str(r_bitrate))
        print('set live streaming time' + str(r_time))
        self.camera.start_recording(self.stream_pipe.stdin,format='h264',bitrate =r_bitrate)
        self.camera.wait_recording(r_time)

    def stop_Youtube_Stream(self):
        #camera.stop_preview()
        print('>> Stop Youtube Sreaming')
        self.camera.stop_recording()
        os.system('killall ffmpeg')
        print('...stop recoding and stop ffmpeg pump to Youtube.')


youtube_stream = YouTube_Stream('tc0h-cgew-sezr-ftyc')
youtube_stream.start_Youtube_Stream(500000,120)
youtube_stream.stop_Youtube_Stream()
