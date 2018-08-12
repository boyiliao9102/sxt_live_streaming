# -*- coding: UTF-8 -*-
import os
import yaml
import sys

CONFIG_FILE = 'apps.yaml'

class Config():
    def __init__(self):
        cfile = os.path.join(os.path.dirname(__file__),CONFIG_FILE).replace("\\","/")
        if os.path.isfile(cfile):
            self.apps = yaml.load(open(cfile))
        else:
            print(CONFIG_FILE + " doesn't exist!")
            sys.exit(2)

    @property
    def Host(self):
        return self.apps['mqttbroker']['host']

    @property
    def Port(self):
        return self.apps['mqttbroker']['port']

    @property
    def Timeout(self):
        return self.apps['mqttbroker']['timeout']

    @property
    def YoutubeStreamURL(self):
        return self.apps['youtube']['streamurl'][0]

    @property
    def YoutubeStreamKey(self):
        return self.apps['youtube']['streamkey']

    @property
    def YoutubeCodec(self):
        return self.apps['youtube']['codec']

    @property
    def YoutubeWidth(self):
        return self.apps['youtube']['resolution']['width']

    @property
    def YoutubeHigh(self):
        return self.apps['youtube']['resolution']['high']

    @property
    def YoutubeFramerate(self):
        return self.apps['youtube']['framerate']

    @property
    def YoutubeBitrate(self):
        return self.apps['youtube']['bitrate']

    @property
    def YoutubeRotation(self):
        return self.apps['youtube']['rotation']

    @property
    def YoutubePeriod(self):
        return self.apps['youtube']['period']


if __name__ == "__main__":
    import doctest
    doctest.testmod()
