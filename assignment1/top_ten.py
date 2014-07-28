import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    
    data = []
    words = {} # initialize an empty dictionary
    topten = {}
    for line in tweet_file:
        data.append(json.loads(line))

    for twitterline in range(0,len(data)):
        entities = data[twitterline].get('entities')
        if entities != None:
            hashtags = entities.get('hashtags')
            for hash in range(0,len(hashtags)):
                text = hashtags[hash].get('text')
                if words.get(text) == None:
                    words[text] = float(1)
                else:
                    words[text] = words.get(text) + 1

    ten = 1
    while ten <= 10:
        maxval = max(words.iteritems(), key=operator.itemgetter(1))[1]
        keys = [k for k,v in words.items() if v==maxval]
        for i in keys:
            if ten <= 10:
                print str(i), words.get(i)
                ten = ten + 1
                del words[i]

if __name__ == '__main__':
    main()
