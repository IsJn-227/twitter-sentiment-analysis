import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

bearer_token = "enter_your_bearer_token_here"

client = tweepy.Client(bearer_token=bearer_token)

query = input("Enter a topic: ")

response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["lang"])

tweets = response.data if response.data else []

positive = 0
neutral = 0
negative = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        positive += 1
    elif polarity == 0:
        neutral += 1
    else:
        negative += 1

labels = ['Positive', 'Neutral', 'Negative']
sizes = [positive, neutral, negative]
colors = ['green', 'blue', 'red']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title(f"Sentiment for '{query}' based on {len(tweets)} tweets")
plt.show()
