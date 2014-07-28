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
        
    test = 'dog'
    newscores = {}
    tweetscore = 5
    test2 = 'cat'
    test3 = 'dog'
    tweetscore2 = 2
    
    for twitterline in range(0,len(data)-1):
        pulltext = data[twitterline].get('text')
        if pulltext != None:
            tweet = pulltext.split()
            a = 0
            count = 0
            for i in tweet:
                count = count + scores.get(i,0)
            for i in tweet:
                if scores.get(test) == None:
                    if newscores.get(i) == None:
                        newscores[i] = [count,float(1)]
                    else:   
                        newscores[i] = [newscores.get(i)[0] + count,newscores.get(i)[1] + 1]  
    

    if scores.get(test) == None:
        if newscores.get(test) == None:
            newscores[test] = [tweetscore,float(1)]
        else:   
            newscores[test] = [newscores.get(test)[0] + tweetscore,newscores.get(test)[1] + 1]

    if scores.get(test2) == None:
        if newscores.get(test2) == None:
            newscores[test2] = [tweetscore,1]
        else:   
            newscores[test2] = [newscores.get(test2)[0] + tweetscore,newscores.get(test2)[1] + 1]
    if scores.get(test3) == None:
        if newscores.get(test3) == None:
            newscores[test3] = [tweetscore2,1]
        else:   
            newscores[test3] = [newscores.get(test3)[0] + tweetscore2,newscores.get(test3)[1] + 1]


    print newscores.keys()
    print newscores.items()
    outputlist = newscores.keys()
    for i in outputlist:
        print i, newscores.get(i)[0]/newscores.get(i)[1]
    

if __name__ == '__main__':
    main()
