import tweepy


consumer_key = "SK5OItiv1BWWPka2yDLzRzijw"
consumer_secret = "maZDODe1X7UqpeF2DiHZY3SEHkKEO0q1qNrmCESmksPrC5DB9H"
access_token = "264393411-5pf360OD2MrAdNy4ttsiYI0CkbzMdUp3ubhKSWJK"
access_token_secret = "9ySEEIhpyHx4snHLHD3tMnDPyj7TipDknss1N8CBQtVyF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
trends=api.trends_places(1) 
for i in trends:
    print i['created_at']+","+i['trends']["name"] 
places=api.trends_available()
for i in places:
    print i['name']+","+i['country']+","+i['woeid']

