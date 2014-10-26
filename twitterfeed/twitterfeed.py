from __future__ import unicode_literals
import twitter
import time
from mcpi import minecraft
try:
    import config
except ImportError:
    raise ImportError('Please define a config.py file. Follow config_sample.py')

api = twitter.Api(consumer_key=config.consumer_key,
                    consumer_secret=config.consumer_secret,
                    access_token_key=config.access_token_key,
                    access_token_secret=config.access_token_secret)

mc = minecraft.Minecraft.create()

most_recent_status_id = None

while True:
    twitter_statuses = api.GetHomeTimeline(since_id=most_recent_status_id)
    if twitter_statuses:
        if most_recent_status_id:
            for twitter_status in twitter_statuses:
                formatted_status = '{}-{}'.format(twitter_status.user.screen_name, 
                    twitter_status.text)
                mc.postToChat(formatted_status.encode('utf-8'))
        most_recent_status_id = twitter_statuses[0].id
        print '-' * 10
    time.sleep(60)
