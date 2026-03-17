# %% [markdown]
# # Represent graph using adjacency matrix
# # Stack, Queue and priority Queue in Python
# # DFS algorithm

# %%
def createMatrix(n):
    m=[]
    for i in range(n):
        r=[]
        for j in range(n):
            r.append(0)
        m.append(r)
    return m

def printMatrix(m):
    for r in m:
        print(r)
        
import queue
def dfs(G,s):
    stack=queue.LifoQueue()
    stack.put(s)
    explore_set=set()
    while not stack.empty():
        node=stack.get()
        if node not in explore_set:
            print(node,end=" ")
            explore_set.add(node)
        for i in range(len(G)):
            if G[node][i]==1:
                if i not in explore_set:
                    stack.put(i)

f=open("graph.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
print(n,m)
G=createMatrix(n)

for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u][v]=1
    #G[v][u]=1
printMatrix(G)
f.close()

dfs(G,0)

# %%
import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(1)
stack.put(20)
print(stack.empty())
print(stack.get())

# %%
import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(1)
stack.put(20)

while not stack.empty():
    print(stack.get())

# %%
import queue
q=queue.Queue()
q.put(10)
q.put(1)
q.put(20)
while not q.empty():
    print(q.get())

# %%
import queue
pq=queue.PriorityQueue()
pq.put((10,"A"))
pq.put((1,"B"))
pq.put((20,"C"))
pq.put((5,"M"))
while not pq.empty():
    print(pq.get())

# %%
def createMatrix(n):
    m=[]
    for i in range(n):
        r=[]
        for j in range(n):
            r.append(0)
        m.append(r)
    return m

def printMatrix(m):
    for r in m:
        print(r)
        
import queue
def bfs(G,s):
    q=queue.Queue()
    q.put(s)
    explore_set=set()
    while not q.empty():
        node=q.get()
        if node not in explore_set:
            print(node,end=" ")
            explore_set.add(node)
        for i in range(len(G)):
            if G[node][i]==1:
                if i not in explore_set:
                    q.put(i)

f=open("graph.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
print(n,m)
G=createMatrix(n)

for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u][v]=1
    #G[v][u]=1
printMatrix(G)
f.close()

bfs(G,0)

# %%
def createList(n):
    m={}
    for i in range(n):
        m[i]=[]
    return m

def printGraph(g):
    for k,v in g.items():
        print(k,v)

import queue
def dfs(G,s):
    stack=queue.LifoQueue()
    stack.put(s)
    explore_set=set()
    while not stack.empty():
        node=stack.get()
        if node not in explore_set:
            print(node,end=" ")
            explore_set.add(node)
        for i in G[node]:
            if i not in explore_set:
                stack.put(i)
  
f=open("graph.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
#print(n,m)

G=createList(n)
for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u].append(v)
    #G[v].append(u)
f.close()
printGraph(G)
dfs(G,0)

# %%
def createList(n):
    m={}
    for i in range(n):
        m[i]=[]
    return m

def printGraph(g):
    for k,v in g.items():
        print(k,v)

import queue
def bfs(G,s):
    stack=queue.Queue()
    stack.put(s)
    explore_set=set()
    while not stack.empty():
        node=stack.get()
        if node not in explore_set:
            print(node,end=" ")
            explore_set.add(node)
        for i in G[node]:
            if i not in explore_set:
                stack.put(i)
  
f=open("graph.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
#print(n,m)

G=createList(n)
for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u].append(v)
    #G[v].append(u)
f.close()
printGraph(G)
bfs(G,0)

# %%



