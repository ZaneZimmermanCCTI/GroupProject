import time as t

adj = 2
adjlist = []



noun = 4
nounlist = []

verb = 2
verblist = []

def getadj():
    for i in range(0,adj):
        adjin = input("Please type an adjective>>>")
        adjlist.append(adjin)

def getnoun():
    for i in range(0,noun):
        nounin = input("Please type a noun>>>")
        nounlist.append(nounin)
    
def getverb():
    for i in range(0,verb):
        verbin = input("Please type a verb (past tense)>>>")
        verblist.append(verbin)

def story():
    print(f'My friend {nounlist[0]} {verblist[0]} to the Ice cream {nounlist[1]}.')
    t.sleep(5)
    print(f'Then, they {verblist[1]} to the {adjlist[0]} {nounlist[2]} coffee shop!')
    t.sleep(5)
    print(f'It was a very {adjlist[1]} {nounlist[3]}!')

def madlibmain():
    getnoun()
    getadj()
    getverb()
    story()
    

