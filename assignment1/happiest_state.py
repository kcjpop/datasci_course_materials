import sys, json, re, string, operator

states = {"Alabama":"AL",
"Alaska":"AK",
"AmericanSamoa":"AS",
"Arizona":"AZ",
"Arkansas":"AR",
"California":"CA",
"Colorado":"CO",
"Connecticut":"CT",
"Delaware":"DE",
"DistrictOfColumbia":"DC",
"FederatedStatesOfMicronesia":"FM",
"Florida":"FL",
"Georgia":"GA",
"Guam":"GU",
"Hawaii":"HI",
"Idaho":"ID",
"Illinois":"IL",
"Indiana":"IN",
"Iowa":"IA",
"Kansas":"KS",
"Kentucky":"KY",
"Louisiana":"LA",
"Maine":"ME",
"MarshallIslands":"MH",
"Maryland":"MD",
"Massachusetts":"MA",
"Michigan":"MI",
"Minnesota":"MN",
"Mississippi":"MS",
"Missouri":"MO",
"Montana":"MT",
"Nebraska":"NE",
"Nevada":"NV",
"NewHampshire":"NH",
"NewJersey":"NJ",
"NewMexico":"NM",
"NewYork":"NY",
"NorthCarolina":"NC",
"NorthDakota":"ND",
"NorthernMarianaIslands":"MP",
"Ohio":"OH",
"Oklahoma":"OK",
"Oregon":"OR",
"Palau":"PW",
"Pennsylvania":"PA",
"PuertoRico":"PR",
"RhodeIsland":"RI",
"SouthCarolina":"SC",
"SouthDakota":"SD",
"Tennessee":"TN",
"Texas":"TX",
"Utah":"UT",
"Vermont":"VT",
"VirginIslands":"VI",
"Virginia":"VA",
"Washington":"WA",
"WestVirginia":"WV",
"Wisconsin":"WI",
"Wyoming":"WY"}

def get_scores(file):
	# Dict to store terms and scores
	scores = {}
	
	for line in file:
		term, score = line.split("\t")
		scores[term] = int(score)

	return scores

def get_state(tweet):
	state = ''
	if 'place' in tweet and tweet['place'] != None and 'full_name' in tweet['place']:
		state = tweet['place']['full_name'].split(',')[0].split(' ')

	if 'user' in tweet and tweet['user'] != None and 'location' in tweet['user']:
		state = tweet['user']['location'].split(',')[0].split(' ')

	state = ''.join(state)
	if state in states:
		return states[state]

	return None

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	# Get the sentiment scores
	scores = get_scores(sent_file)
	results = {}
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	# Calculate state's happiness
	for tweet in tweet_file:
		# Convert JSON to dictionary
		tweet = json.loads(tweet)

		# Skip non-English tweets
		if 'lang' in tweet and tweet['lang'] != 'en':
			continue
		# Get the state
		state = get_state(tweet)

		# Skip if we cannot find the state
		if state == None:
			continue

		if state not in results:
			results[state] = 0.0

		# Parse the text
		tweet['text'] = regex.sub('', tweet['text'])

		# Split by whitespace
		terms = tweet['text'].split()
		for term in terms:
			if term in scores:
				results[state] += scores[term]

	# Sort the result
	sort = sorted(results.iteritems(), key=operator.itemgetter(1))
	sort.reverse()

	# Get the first one
	print sort[0][0]

if __name__ == '__main__':
		main()