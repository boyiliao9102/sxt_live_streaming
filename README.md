

Sanxiantai Live Stream Task
===========================

Using MQTT to trigger live streaming on Youtube and Facebook.
All the processes tests on raspberry pi.

## How To Use

To Run the following command for starting this service

    python main.py

Then use any MQTT client to public to a topic:

    mosquitto_pub -t 'livestream/youtube/start' -m test

## Topics

    livestream/youtube/start
    livestream/youtube/stop
    livestream/facebook/start
    livestream/facebook/stop
