
import graphs as G

#Modified and followed techniques from graphs.py spanTree method to add additional logic for handling data
def spanningTree(start, N , D = None, parents = None):
    if parents is None:
        parents = { start: None}
        D = { start } 

 #Produce dictionary with key (v) the jump result function (N) and with value (u) the parent from D
    DnewP = {v:u for u in D for v in N(u) if v not in parents } 
    if len(DnewP) == 0: return (None,None)
    Dnew =  {k for k in DnewP.keys() } #get only jump result value from DnewP

    parents.update(DnewP)

    result = next((v for v in parents if GameOver(v)), None)

    if result is not None:
        return (parents,result)

    return spanningTree(start,N,Dnew,parents)

   
#Modified and followed techniques from CAB203 sample code eight.py to add end result and detect None returned for parents and result
def shortestPath(start,N):
    (parents,end) = spanningTree(start,N)
    if parents is None and end is None:return None
    return G.pathFromTree(parents,end)

#Check if game has ended and if only 1 peg is remaining
def GameOver(v):
    return v.count('X') == 1

#Modified and followed techniques from CAB203 sample code eight.py swap function 
def jump(puzzle, i, j):
    ret = list(puzzle)
    ret[i] = 'o'
    ret[j] = 'X'
    if i < j: #jump to the right
        ret[i + 1] = 'o'
    else:   #jump to the left
        ret [i - 1] = 'o'
    return tuple(ret)

#Helper functions to check if peg is able to jump left / right
def jumpToLeft(puzzle,i):
    return puzzle[i] == 'X' and i-2 >= 0 and puzzle[i-1] == 'X' and puzzle[i-2] == 'o'

def jumptoRight(puzzle,i):
    return puzzle[i] == 'X' and i+2 < len(puzzle) and puzzle[i+1] == 'X' and puzzle[i+2] =='o'

#Modified and followed techniques from CAB203 sample code eight.py 
def N(v):
    r = set()
    for i in range(len(v)):
        if v[i] == 'X':
            if jumptoRight(v,i):
                r.add(jump(v,i, i+2))
            if jumpToLeft(v,i):
                r.add(jump(v,i,i-2))

    return r

#Modified and followed techniques from CAB203 sample code eight.py 
def findmove(u,v):
    for i in range(len(u)):
        if u[i] != v[i]:
            if v[i] == 'X':
                return (i+2, 'L')
            else:
                return (i,'R')
    return None


def pegsSolution(gameBoard):
   # Program your solution here
   start = tuple(gameBoard) #convert make gameBoard variable as tuple
   path = shortestPath(start,N)
   if path is None: return None
   sequenceofMoves = [findmove(u,v) for u,v in zip(path[:-1], path[1:]) ]
   return sequenceofMoves


## TEST HARNESS
# The following will be run if you execute the file like python3 pegs_n1234567.py
# Your solution should not depend on this code.
# You may wish to add your own test cases.
if __name__ == '__main__':
   gameBoard = 'ooXXXoXoXX' 
   print(pegsSolution(gameBoard))
