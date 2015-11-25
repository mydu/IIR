#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 

consumer_key = "SK5OItiv1BWWPka2yDLzRzijw"
consumer_secret = "maZDODe1X7UqpeF2DiHZY3SEHkKEO0q1qNrmCESmksPrC5DB9H"
access_token = "264393411-5pf360OD2MrAdNy4ttsiYI0CkbzMdUp3ubhKSWJK"
access_token_secret = "9ySEEIhpyHx4snHLHD3tMnDPyj7TipDknss1N8CBQtVyF"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['paris'],languages = ['en'])