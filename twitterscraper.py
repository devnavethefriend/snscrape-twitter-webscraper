# import necessary modules
import snscrape.modules.twitter as sntwitter
import pandas as pd

# set search query to "web scraping" & limit search to 1000 tweets
query = "web scraping"
limit = 1000

# create empty list and for loop function to extract data, breaks when limit is reached
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent])

# create pandas dataframe which saves the extracte data into a csv and json file
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
df.to_csv('scraped-tweets.csv', index=False, encoding='utf-8')
df.to_json('scraped-tweets.json', orient='records', lines=True)
