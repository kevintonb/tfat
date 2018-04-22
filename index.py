import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

def main():
	#Reading Tweets
	print 'Reading Tweets\n'
	tweets_data_path = 'twitter_data.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue

	print 'Structuring Tweets\n'
	tweets = pd.DataFrame()
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	print len(tweets_data)

	key1 = raw_input("Keyword 1 :\n")
	key2 = raw_input("Keyword 2 :\n")
	key3 = raw_input("Keyword 3 :\n")
	print 'Adding user keyword tags to the data\n'
	tweets[key1] = tweets['text'].apply(lambda tweet: word_in_text(key1, tweet))
	tweets[key2] = tweets['text'].apply(lambda tweet: word_in_text(key2, tweet))
	tweets[key3] = tweets['text'].apply(lambda tweet: word_in_text(key3, tweet))

	print 'Analyzing tweets by user keyword\n'
	keyword_input = [key1, key2, key3]
	tweets_by_keyword_input = [tweets[key1].value_counts()[True], tweets[key2].value_counts()[True], tweets[key3].value_counts()[True]]
	x_pos = list(range(len(keyword_input)))
	width = 0.8
	fig, ax = plt.subplots()
	plt.bar(x_pos, tweets_by_keyword_input, width, alpha=1, color='g')
	ax.set_ylabel('Number of tweets', fontsize=15)
	ax.set_title('Ranking: key1 vs. key2 vs. key3 (Raw data)', fontsize=10, fontweight='bold')
	ax.set_xticks([p + 0.4 * width for p in x_pos])
	ax.set_xticklabels(keyword_input)
	plt.grid()
	plt.savefig('tweet_by_keyword_input', format='png')

if __name__=='__main__':
	main()