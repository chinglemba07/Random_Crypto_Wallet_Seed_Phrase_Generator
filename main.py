import random
fours=[]
fives=[]
sixes=[]
sevens=[]

with open('wordlist.txt') as wordlist:
    for line in wordlist:
        #print(line)
        if len(line.strip())==4:
            fours.append(line.strip())
        elif len(line.strip())==5:
            fives.append(line.strip())
        elif len(line.strip())==6:
            sixes.append(line.strip())
        elif len(line.strip())==7:
            sevens.append(line.strip())
# print(len(fours))
# print(len(fives))
# print(len(sixes))
# print(len(sevens))

fivesLess=[]
sixesLess=[]
sevensLess=[]

fivesCounter=0
while fivesCounter < len(fours):
    randFive=random.choice(fives)
    if randFive not in fivesLess:
        fivesLess.append(randFive)
        fivesCounter +=1

sixesCounter=0
while sixesCounter < len(fours):
    randSix=random.choice(sixes)
    if randSix not in sixesLess:
        sixesLess.append(randSix)
        sixesCounter +=1

sevensCounter=0
while sevensCounter < len(fours):
    randSeven=random.choice(sevens)
    if randSeven not in sevensLess:
        sevensLess.append(randSeven)
        sevensCounter +=1

# print(len(fivesLess))
# print(len(sixesLess))
# print(len(sevensLess))

choices=[fours,fivesLess, sixesLess, sevensLess]

seedCounter=0
while seedCounter<1:
    seed=[]
    while len(seed)<12:
        wordLengthChoice=random.choice(choices)
        wordChoice=random.choice(wordLengthChoice)
        seed.append(wordChoice)
    seedCounter += 1
    

# for i in range(len(seed)):
#     print("{} : {}".format(i+1,seed[i]))
print("Random seed phrases for your wallet :")
print(seed)
