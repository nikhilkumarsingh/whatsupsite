import twitter
import re


consumer_key='WXrRsb0WBiqw2JefGzdbI15jZ'
consumer_secret='XlhjVbue1rXVyzPpo4ywEDURGtQLgF1kdLPM1PmByuyDPrdqTL'
access_token_key='749944468212625408-4Bw8QR9IMCMKDIBCIOexGWcxVLvqUAY'
access_token_secret='YY943k0KMeQwQT0CeisR7A6X42Mwr3JVxjnFJ7bDMMiGb'


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


