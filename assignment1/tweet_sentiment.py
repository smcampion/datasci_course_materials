import sys
import json

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
    output = []
    twitterline = 0
    while twitterline < len(data):
        pulltext = data[twitterline].get('text',0)
        if pulltext != 0:
            x = pulltext.split()
            a = 0
            count = 0
            for i in x:
                count = count + scores.get(i,0)
                if count != 0:
                    a = 1
            if a == 1:
                print count
                output.append(count)
        twitterline = twitterline +1
#    print len(output)

if __name__ == '__main__':
    main()
