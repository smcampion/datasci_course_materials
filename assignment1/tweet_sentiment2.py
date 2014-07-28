import sys
import json

def dic_afinn(file):
    afinnfile = open(file)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

#    print scores.items() # Print every (term, score) pair in the dictionary
    print scores['absentee']
    key = 'dog'
    print scores.get(key,'0')

def dic_tweet(file):
    tweetfile = open(file)
    scores = {} # initialize an empty dictionary
    for line in tweetfile:
        term, score  = json.loads  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    print scores.items() # Print every (term, score) pair in the dictionary

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#    lines(sent_file)
#    lines(tweet_file)
    data = []
    scores = {} # initialize an empty dictionary
    for line in tweet_file:
#        data = json.loads(line)
#        print data['text']
        data.append(json.loads(line))
    print data[10].get('text')
    x = data[10].get('text').split()
#    print data[0].find('status')
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    count = 0
    for i in x:
        print scores.get(i,0)
        count = count +scores.get(i,0)
    print count
 #   print len(data)
 #   print data['text']

if __name__ == '__main__':
    main()
