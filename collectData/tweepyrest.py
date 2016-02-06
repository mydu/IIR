import tweepy
import sqlite3
import time
import csv #Import csv

# db = sqlite3.connect('data/ParisAttack.db')
# # Get a cursor object
# cursor = db.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS ParisTable(id INTEGER PRIMARY KEY, time TEXT, status TEXT, geo TEXT, place TEXT,user_location TEXT)''')
# db.commit()
#Variables that contains the user credentials to access Twitter API 
consumer_key = "SK5OItiv1BWWPka2yDLzRzijw"
consumer_secret = "maZDODe1X7UqpeF2DiHZY3SEHkKEO0q1qNrmCESmksPrC5DB9H"
access_token = "264393411-5pf360OD2MrAdNy4ttsiYI0CkbzMdUp3ubhKSWJK"
access_token_secret = "9ySEEIhpyHx4snHLHD3tMnDPyj7TipDknss1N8CBQtVyF"


csvFile = open('result17en.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

search="*"

c=tweepy.Cursor(api.search, 
                    q=search, 
                    since="2015-11-21", 
                    until="2015-11-22",
                    geocode='48.8566667,2.3509871,30km',
                    count=100,lang="en").items()
while True:
	try:
		tweet = c.next()
		if tweet.place!=None:
			# geo=tweet.place.bounding_box.coordinates[0]
			place=tweet.place.full_name+","+tweet.place.country
		else:
			# geo="NA"
			place="NA"
		print tweet.text
		if ()
		hashtag=" ".join([i["text"].encode("utf-8") for i in tweet.entities.get('hashtags')])
		# csvWriter.writerow([tweet.created_at,tweet])
		# cursor.execute('''INSERT INTO ParisTable(time,status,geo,place,user_location) VALUES(?,?,?,?,?)''' ,(tweet.created_at, unicode(tweet.text),place,str(geo),unicode(tweet.user.location.encode)))
		csvWriter.writerow([tweet.created_at,tweet.text.encode("utf-8"),hashtag,place.encode("utf-8"),tweet.user.location.encode("utf-8")])
	except tweepy.TweepError:
		print "Error! Failed to get access token!"
		time.sleep(60 * 15)
		continue
	except StopIteration:
		break  
# db.commit() 
# db.close()
csvFile.close()

# csvFile = open('result13.csv', 'a')
# #Use csv Writer
# csvWriter = csv.writer(csvFile)
# # results = api.search(q="ParisAttack", geocode='48.8566667, 2.3509871,10km', count=100)

# for tweet in tweepy.Cursor(api.search, 
#                     q="*", 
#                     since="2015-11-13", 
#                     until="2015-11-14",
#                     geocode='48.8566667,2.3509871,20km').items(999999):
	
# 	if tweet.place!=None:
# 		geo=tweet.place.bounding_box.coordinates[0]
# 		place=tweet.place.full_name+","+tweet.place.country
# 	else:
# 		geo="NA"
# 		place="NA"
# 	csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),place,geo,tweet.user.location.encode('utf-8')])
# csvFile.close()