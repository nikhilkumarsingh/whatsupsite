import twitter
import re


consumer_key=
consumer_secret=
access_token_key=
access_token_secret=


def search_twitter(query):
   api = twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret) 
   tweets=api.GetSearch(query,count=75,lang="en")
   tw=[]
   for tweet in tweets:
     tw.append(tweet.text)
   words = ' '.join(tweet for tweet in tw)
   words = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])

   words = re.sub("[^a-zA-Z]+", " ", words)
   words=words.replace("amp","")
   return words,tweets


