def get_scores(file):
  # Dict to store terms and scores
  scores = {}
  
  for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)

  return scores
