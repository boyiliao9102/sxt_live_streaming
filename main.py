# -*- coding: UTF-8 -*-
import sys
import getopt
import paho.mqtt.client as mqtt   # pip install paho-mqtt
from config import Config
from topic  import Topic
from youtubelive import YoutubeLive
#from facebooklive import FacebookLive

conf  = Config()
topic = Topic()

def on_connect(client, userdata, flags, rc):
    print("Connected to {0} with result code {1}".format(conf.Host, rc))
    # Subscribe to LiveStream topics
    client.subscribe(topic.AllLiveStream)


def on_message(client, userdata, msg):
    print("Message received on topic {0}: {1}".format(msg.topic, msg.payload))
    if (msg.topic.startswith(topic.YoutubeTopics) == True):
        livestream = YoutubeLive()
    elif (msg.topic.startswith(topic.FacebookTopics) == True):
        print("livestream = FacebookLive()")
    else:
        print("The topic doesn't support")
    livestream.process(msg.topic)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(conf.Host, conf.Port, conf.Timeout)
client.loop_forever()

