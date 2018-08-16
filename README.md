
Sanxiantai Live Streaming
===========================

Using MQTT to trigger live streaming on Youtube and Facebook.
All the processes tests on raspberry pi.

## How To Use

To Run the following command for starting this service

    python3 main.py

Then use any MQTT client to public to a topic:

    mosquitto_pub -t 'livestream/youtube/start' -m test
    mosquitto_pub -t 'livestream/youtube/stop' -m test

## Topics

    livestream/youtube/start
    livestream/youtube/stop
    livestream/facebook/start(not support)
    livestream/facebook/stop(not support)
