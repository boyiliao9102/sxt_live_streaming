# -*- coding: UTF-8 -*-

TOPIC_LIVESTREAM = {
    "youtube_Start"     : "livestream/youtube/start",
    "youtube_Stop"      : "livestream/youtube/stop",
    "youtube_Topics"    : "livestream/youtube/",
    "facebook_Start"    : "livestream/facebook/start",
    "facebook_Stop"     : "livestream/facebook/stop",
    "facebook_Topics"   : "livestream/facebook/",
    "all_Topics"        : "livestream/#"
}

class Topic():
    def __init__(self):
        self.livestream = TOPIC_LIVESTREAM

    @property
    def YoutubeStart(self):
        return self.livestream['youtube_Start']

    @property
    def YoutubeStop(self):
        return self.livestream['youtube_Stop']

    @property
    def YoutubeTopics(self):
        return self.livestream['youtube_Topics']

    @property
    def FacebookStart(self):
        return self.livestream['facebook_Start']

    @property
    def FacebookStop(self):
        return self.livestream['facebook_Stop']

    @property
    def FacebookTopics(self):
        return self.livestream['facebook_Topics']

    @property
    def AllLiveStream(self):
        return self.livestream['all_Topics']

if __name__ == "__main__":
    import doctest
    doctest.testmod()
