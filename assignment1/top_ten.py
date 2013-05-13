import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    # Dict to contain all hashtags
    hashtags = {}

    for line in tweet_file:
        # Convert to dict
        tweet = json.loads(line)
        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            for tag in tweet['entities']['hashtags']:
                if tag['text'] in hashtags:
                    hashtags[tag['text']] += 1.0
                else:
                    hashtags[tag['text']] = 1.0

    # Sort the hashtag
    sort = sorted(hashtags.iteritems(), key=operator.itemgetter(1))
    sort.reverse()

    # Slice the tuble
    sort = sort[:10]
    
    # Print the sort result
    for item in sort:
        print item[0] + ' ' + str(item[1])

if __name__ == '__main__':
    main()