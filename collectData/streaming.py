
# coding: utf-8

# ### Import the necessary methods from tweepy library :

# In[2]:

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import csv


# ### Variables that contains the user credentials to access Twitter API :

# In[44]:

consumer_key = "SK5OItiv1BWWPka2yDLzRzijw"
consumer_secret = "maZDODe1X7UqpeF2DiHZY3SEHkKEO0q1qNrmCESmksPrC5DB9H"
access_token = "264393411-5pf360OD2MrAdNy4ttsiYI0CkbzMdUp3ubhKSWJK"
access_token_secret = "9ySEEIhpyHx4snHLHD3tMnDPyj7TipDknss1N8CBQtVyF"
GEOBOX_WORLD = [-180,-90,180,90]
GEOBOX_PARIS = [2.225193,48.815573,2.469921,48.902145]
GEOBOX_FRANCE=[-5.14,41.34,9.56,51.09]
GEOBOX_EUROPE =[-31.5,34.5,74.4,82.2]


# ### This is a basic listener that just prints received tweets to stdout :

# In[ ]:

writer=csv.writer(open('europe.csv','wb'))
writer.writerow(["time","text","hashtag","place","geobox"])
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            tweet = json.loads(data)
            time=tweet["created_at"]
            text=tweet["text"].encode('ascii', 'ignore')
            hashtag=" ".join([i["text"].encode('ascii', 'ignore') for i in tweet['entities']['hashtags']])
            place=tweet['place']['full_name'].encode('ascii', 'ignore')
            geobox=tweet['place']['bounding_box']['coordinates']
            writer.writerow([time,text,hashtag,place,geobox])
            # writer.writerow([status["created_at"], status["text"].encode('ascii', 'ignore')])
            print tweet["created_at"]
            # print status['text'].encode('ascii', 'ignore')
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=GEOBOX_EUROPE,languages = ['en'])


# In[30]:

print type(str('asdfa'))
print type(None)


# In[ ]:



