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
        
    newscores = {}
    
    for twitterline in range(0,len(data)-1):
        pulltext = data[twitterline].get('text')
        if pulltext != None:
            tweet = pulltext.split()
            count = 0
            for i in tweet:
                count = count + scores.get(i,0)
            for i in tweet:
                if scores.get(i) == None:
                    if newscores.get(i) == None:
                        newscores[i] = [count,float(1)]
                    else:   
                        newscores[i] = [newscores.get(i)[0] + count,newscores.get(i)[1] + 1]  
    
    outputlist = newscores.keys()
    for i in outputlist:
        print i, newscores.get(i)[0]/newscores.get(i)[1]
    

if __name__ == '__main__':
    main()
