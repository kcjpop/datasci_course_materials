import sys
import json

def get_scores(file):
  # Dict to store terms and scores
  scores = {}
  
  for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)

  return scores

def process_tweet(line, scores):
    score = 0.0
    tweet = json.loads(line)

    if tweet.has_key('lang') and tweet['lang'] != 'en':
        return score

    if tweet.has_key('text'):
        words = tweet['text'].split() # Split all whitespaces
        for word in words:
            word = word.strip().lower()
            if word in scores:
                score += scores[word]

    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Get sentiment scores
    scores = get_scores(sent_file)

    # Process the tweet file, is it a pain?
    for line in tweet_file:
        print process_tweet(line, scores)

if __name__ == '__main__':
    main()
