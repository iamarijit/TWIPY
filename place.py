import tweepy
from tweepy.auth import OAuthHandler
import pandas as pd
consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
access_token_key = 'ACCESS TOKEN KEY'
access_token_secret = 'ACCESS TOKEN SECRET'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
def place():
 trend = list(api.trends_available())
 name = []
 country = []
 woeid = []
 countryCode = []
 dataset = []
 for i in trend:
 name.append(i['name'])
 country.append(i['country'])
 woeid.append(i['woeid'])
 countryCode.append(i['countryCode'])
 dataset = list(zip(country, countryCode, name, woeid))
 data = pd.DataFrame(data=dataset, columns=['Country', 'Country_code',
'Place', 'ID'])
 data.to_csv('places.csv', encoding='utf-8', index=False)
