# %% [markdown]
# # Graph Representation
# - Adjacency Matrix
# - Adjacency List

# %% [markdown]
# # Read/Write File in python

# %%
# Read -- r
# write -- w
# append -- a
f=open("Hello.txt","w")
f.write("I love Python\n")
f.write("I love AI")
f.close()

# %%
import random
f=open("100.txt","w")
for i in range(100):
    f.write(str(random.randint(1,1000))+"\n")
f.close()

# %%
f=open("Hello.txt","w")
f.write("I love Bangladesh")
f.close()

# %%
f=open("1.txt","r")
content=f.read()
print(content)
list=content.split()
print(list)

# %%
f=open("1.txt","r")
line=f.readline()
print(line)
line=f.readline()
print(line)

# %%
f=open("1.txt","r")
for i in range(3):
    line=f.readline()
    list=line.split()
    print(list)
    print(list[0])

# %% [markdown]
# # input from graph

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

# %%



