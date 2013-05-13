import sys, json, re, string

def get_scores(file):
	# Dict to store terms and scores
	scores = {}
	
	for line in file:
		term, score = line.split("\t")
		scores[term] = int(score)

	return scores

def get_terms(tweet):
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	tweet['text'] = regex.sub('', tweet['text'])
	return tweet['text'].split()

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	# Dict to contain unknown terms
	unknown = {}

	# Get the scores
	scores = get_scores(sent_file)

	# List of new tweets
	new_tweets = []
	for tweet in tweet_file:
		# Convert JSON to dict
		tweet = json.loads(tweet)

		# Skip non-English tweets
		if 'lang' in tweet and tweet['lang'] != 'en':
			continue

		# Skip empty text
		if 'text' not in tweet:
			continue
		
		terms = get_terms(tweet)
		sentiment = 0.0
		for term in terms:
			if term not in scores:
				if term not in unknown:
					unknown[term] = 1.0
				else:
					unknown[term] += 1.0
			else:
				# Calculate the sentiment of this tweet
				sentiment += scores[term]

		tweet['sentiment'] = sentiment
		# Add to new list to reduce number of tweets
		new_tweets.append(tweet)

	for tweet in new_tweets:
		terms = get_terms(tweet)
		for term in terms:
			if term not in scores:
				val = float(tweet['sentiment'] / unknown[term])
				print "%s %.3f"%(term.replace(' ', '%20').encode("utf8"),float(val))

if __name__ == '__main__':
	main()
