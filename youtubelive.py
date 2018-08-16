# -*- coding: UTF-8 -*-
import os
import time
import io
import picamera  # pip3 install picamera
import subprocess
from config import Config
from topic  import Topic

FFMPEG_CMD='ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv '

class YoutubeLive():
    def __init__(self):
        self.conf   = Config()
        self.topic  = Topic()
        self.camera = picamera.PiCamera()

    def stop_Youtube_Stream(self):
        print('>> Stop Youtube Sreaming')
        self.camera.stop_recording()
        #os.system('killall ffmpeg')
        #subprocess.call('killall ffmpeg', shell=True)
        try:
            output = subprocess.check_output('killall ffmpeg', shell=True)
        except subprocess.CalledProcessError:
            print('kill ffmpeg Exception handled')

        print('...stop recoding and stop ffmpeg pump to Youtube.')


    def start_Youtube_Stream(self):
        STREAM_URL = self.conf.YoutubeStreamURL
        STREAM_KEY = self.conf.YoutubeStreamKey
        STREAM_CMD = FFMPEG_CMD + STREAM_URL + STREAM_KEY

        self.stream_pipe = subprocess.Popen(STREAM_CMD, shell=True, stdin=subprocess.PIPE)
        print('>> init Youtube')
        print(self.conf.YoutubeWidth)
        #self.camera.resolution = (int(self.conf.YoutubeWidth), int(self.conf.YoutubeHigh))
        self.camera.resolution = (self.conf.YoutubeWidth, self.conf.YoutubeHigh)
        self.camera.rotation   = self.conf.YoutubeRotation
        self.camera.framerate  = self.conf.YoutubeFramerate
        rgb = bytearray(self.camera.resolution[0] * self.camera.resolution[1] * 3)
        print('>> Start Youtube Sreaming')
        self.camera.start_recording(self.stream_pipe.stdin, format=self.conf.YoutubeCodec, bitrate=self.conf.YoutubeBitrate)
        #self.camera.wait_recording(self.conf.YoutubePeriod)
        #self.stop_Youtube_Stream()

    def process(self, triggered_topic):
        if (self.topic.YoutubeStart == triggered_topic):
            self.start_Youtube_Stream()
        elif (self.topic.YoutubeStop == triggered_topic):
            self.stop_Youtube_Stream()
            print(">> process stop YouTube!")
        else:
            print("The topic doesn't support!")
