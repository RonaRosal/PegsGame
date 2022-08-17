def N(V, E, u):
   """Return the neighbourhood of vertex u in graph (V, E)"""
   return { v for v in V if (u,v) in E }

def NS(V, E, S):
   """Return the neighbourhood of a set of vertices S in graph (V, E)"""
   return { v for v in V for u in S if (u,v) in E }

def distanceClasses(V, E, u):
   """Given a graph (V,E) and a starting vertex u, outputs a list of distances classes.  That is, returns a partition of the vertices into sets of fixed distances from u, where u is in the distance class for distance 0.  Behaviour is undefined if the graph is disconnected."""
   V0 = V              # V_0 = V
   D = [ {u} ]         # D[0] = D_0 = {u}
   return distanceClassesR(V0, E, D)

def distanceClassesR(V, E, D):
   Vnew = V - D[-1]            # V_{j} = V_{j-1} / D_{j-1}
   if len(Vnew) == 0: return D # Already considered all elements?
   Dnew = D + [ NS(Vnew, E, D[-1]) ]  # D_{j} = N_{V_j}(D_{j-1})
   return distanceClassesR(Vnew, E, Dnew)

def arbitrary(S):
   """Return an arbitrary element of the set S"""
   return next(iter(S))

def spanTree(V, E, r):
   """Find a spanning tree in graph (V,E) rooted on r where all paths from vertex r to other vertices are shortest.  If the graph is disconnected then the spanning tree only covers the component containing r.
   
   The tree is returned as a dictionary where keys are vertices and values are the parent of that vertex in the spanning tree."""
   parents = { r: None } 
   spanTreeR(V - {r}, E, {r}, parents)
   return parents 

def spanTreeR(V, E, D, parents):
   Dnew = NS(V, E, D)
   if len(Dnew) == 0: return
   for v in Dnew:
      parents[v] = arbitrary(N(D, E, v))
   spanTreeR(V - Dnew, E, Dnew, parents)

def pathFromTree(parents, v):
   """Find a shortest path from the root to vertex v in a tree.  The tree must be given as a dictionary where keys are vertices and values are the parent verticex of the key.  The path is returned as a list of vertices starting from the root and ending at v (inclusive).  Behaviour is undefined if there is no such path."""
   u = parents[v]
   if u == None: return [v]      # at root? Stop
   return pathFromTree(parents, u) + [v] # go to parent, then to v

def solveSpp(V, E, start, end):
   """Solve the shortest path problem in graph (V,E) from vertex start to vertex end.  Behaviour is undefined if there is no such path."""
   parents = spanTree(V, E, start)
   return pathFromTree(parents, end)

def bfs(D, NS, process, Dold = None):
   """ Perform a breadth-first search on a tree.  
   D = Starting set of vertices
   NS = A function that returns the neighbourhood of a set
   
   process(D, Dold) = a function that processes vertices in D given the previous distance class.  If the return value is true then the search terminates.

   bfs will terminate if process(D, Dold) returns True or if NS returns no unseen vertices.
   """
   if Dold == None: Dold = set()    # base case
   if process(D, Dold): return   
   Dnew = NS(D) - D - Dold          # new distance class
   if not Dnew: return              # return if Dnew empty
   return bfs(Dnew, NS, process, D)

