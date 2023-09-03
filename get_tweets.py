# import required libraries
'''import tweepy
import time
import pandas as pd
pd.set_option('display.max_columns', None , 'display.width' , 5000 , 'display.max_rows' , 25 )

# api key
api_key = "twpGNz7nnJgDPspimKZUjb0fw"
# api secret key
api_secret_key = "mQz4F2gsv8x4YEnaUZ2oXiAz9ski4HMLpScd7CyfDEKta3JhGP"
# access token
access_token = "1319261429267009536-lUlczkxsWg3DaKFbLw9jl1bWh5eaFR"
# access token secret
access_token_secret = "lV25Begi1QddmJmers9uel5ht0PtKgUVtjztK1cmTp30P"


# authorize the API Key
authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)


# call the api
api = tweepy.API(authentication, wait_on_rate_limit=True)


def get_related_tweets(text_query):
    print("Entering get tweets")
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 5
    try:
        # Pulling individual tweets from query
        for tweet in api.search_tweets(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)'''
# import required libraries
'''import tweepy
import time
import pandas as pd
pd.set_option('display.max_columns', None , 'display.width' , 5000 , 'display.max_rows' , 25 )
# client id = Q2phbWFuU1pCZGVrZlVRc3k5RDA6MTpjaQ
# client secret=ISIop9Uf0M07EPG8EgpQad8qxS6J_sCCqO1UIVyW4gwApOyEVA
# api key
api_key = "omY4KUIbsEx3B0UKRLC1UbXb9"
# api secret key
api_secret_key = "brW63fCJaCe0r0ZZk4rlNTbLKj7C6oaK7kUG8z31fsX9JZxqqZ"
# bearer token AAAAAAAAAAAAAAAAAAAAAB0ZpgEAAAAAazz%2BolH4W3%2FNE0fyIHH1rGim2lw%3D2QPXL1AeVk97Ohv0BEdk9siu8g1kBjQHQnJyIs6cpaSKpYvyR2
access_token = "1693698858679926787-A0DYn8W9gbrMc6N5sllrOBhYvHBADW"
# access token secret
access_token_secret = "v8pF9fE9948Yzcxx5xBxXZaxFNAOnr0fydmcAZIDaHaPv"


# authorize the API Key
#authentication = tweepy.OAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
#authentication.set_access_token(access_token, access_token_secret)


# call the api
#api = tweepy.API(authentication, wait_on_rate_limit=True)
#auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAJrDKwEAAAAANa1%2B44FAW08s94qpEpdIT5as70c%3D9XxOfMiPP4SKEJrJbgXk8LiaYC6dlTsugkk1bZDOAAoqX6MelB")
#api = tweepy.API(auth)
auth = tweepy.OAuth1UserHandler(
   api_key, api_secret_key,
   access_token, access_token_secret
)
api = tweepy.API(auth)
def get_related_tweets(text_query):
    print("Entering get tweets")
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 5
    try:
        # Pulling individual tweets from query
        for tweet in api.search_tweets(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)'''
# import required libraries
import tweepy
import requests
import time
import googleapiclient.discovery
import pandas as pd
pd.set_option('display.max_columns', None , 'display.width' , 5000 , 'display.max_rows' , 25 )


"""
# api key
api_key = "O0XOvJkKNWnDrU5Vgrtw4DHBe"
# api secret key
api_secret_key = "d5dPpw95tiDQRgnsEzc7KuIdXGIqq79wb7GR528QUogz5TsmPD"
# access token
access_token = "1319261429267009536-KUhIuKTXm2jhRAVlqVkqzIClEMHTBC"
# access token secret
access_token_secret = "WJiZkGQkdxlqiWr9g1bSAWhKkLjOaQkHZopkA3rHhhNC7"


# authorize the API Key
authentication = tweepy.AppAuthHandler(api_key, api_secret_key)

# authorization to user's access token and access token secret
#authentication.set_access_token(access_token, access_token_secret)


# call the api
#api = tweepy.API(authentication, wait_on_rate_limit=True)
#api = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAJrDKwEAAAAA7A1AEnPGTVG%2BNBDYPpwraNO4wWY%3DRzZf2FfsA9ZV1jCzhI2JY103NYw6zkFj9qM6gz132bCJvyKDm8")


# Replace with your own credentials
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJrDKwEAAAAA7A1AEnPGTVG%2BNBDYPpwraNO4wWY%3DRzZf2FfsA9ZV1jCzhI2JY103NYw6zkFj9qM6gz132bCJvyKDm8'

# Search for tweets based on a keyword
#search_query = 'your_search_keyword'
 # Number of tweets to retrieve

# Construct the API endpoint
base_url = 'https://api.twitter.com/2/tweets/search/recent'
headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}


# Make the API request
#



"""

api_service_name = "youtube"
api_version = "v3"
"your developer key here"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)





def get_related_tweets(text_query):
    print("Entering get tweets")
    request = youtube.commentThreads().list(
        part="snippet",
        videoId="Qk5iTy-0Ewk",
        maxResults=100,
        searchTerms=text_query,
        textFormat="plainText"
    )
    response = request.execute()

    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 5
    #params = {'query': text_query, 'max_results': count}
    try:
        
        # Pulling individual tweets from query
        #for tweet in api.search_tweets(q=text_query,count=count):
        #response = requests.get(base_url, headers=headers, params=params)
        print("FAIL")
        """
        for tweet in  requests.get(base_url, headers=headers, params=params):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})"""
        
        print("SUCCESS")
        #tweets = response.json()['data']
        for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                tweets_list.append([
                        comment['authorDisplayName'],
                        comment['publishedAt'],
                        comment['updatedAt'],
                        comment['likeCount'],
                        comment['textDisplay']
    ])
        return pd.DataFrame(tweets_list, columns=['author', 'published_at', 'updated_at', 'like_count', 'tweet_text'])


    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)
