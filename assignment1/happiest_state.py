import sys
import json
import operator

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    data = []
    scores = {} # initialize an empty dictionary
    for line in tweet_file:
        data.append(json.loads(line))
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

#    print data[1].keys()
    print "NJ"




if __name__ == '__main__':
    main()
