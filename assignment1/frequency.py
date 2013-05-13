import sys
import re
import string
import json

def main():
    tweet_file = open(sys.argv[1])
    # Dict to contain all string
    terms = {}
    total_occurences = 0.0
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    for line in tweet_file:
        # Convert JSON to dictonary
        line = json.loads(line)
        
        # Skip non-English tweets
        if 'lang' in line and line['lang'] != 'en':
            continue

        if 'text' in line:
            # Remove all punctuation        
            line['text'] = regex.sub('', line['text'])

            # Split by whitespace
            tokens = line['text'].split()
            for token in tokens:
                if token in terms:
                    terms[token] += 1.0
                else:
                    terms[token] = 1.0

                total_occurences += 1.0

    # Calculate the histogram
    results = {}
    for term in terms.items():
        print term[0] + ' ' + str(term[1] / total_occurences)

if __name__ == '__main__':
    main()