import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    
    data = []
    words = {} # initialize an empty dictionary
    for line in tweet_file:
        data.append(json.loads(line))
    totalwords = float(0)
    
    for twitterline in range(0,len(data)-1):
        pulltext = data[twitterline].get('text')
        if pulltext != None:
            tweet = pulltext.split()
            count = 0
            for i in tweet:
                totalwords = totalwords + 1
                if words.get(i) == None:
                    words[i] = 1
                else:
                    words[i] = words.get(i) + 1
    
    for i in words.keys():
        print i, words.get(i)/totalwords
    

if __name__ == '__main__':
    main()
