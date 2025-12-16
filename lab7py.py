# %% [markdown]
# # Dictionary in python (Key value pair)
# - Map/Hashmap
# 
# # Graph using adjacency List

# %%
print("Welcome to Lab Exam1")

# %%
cgpa={
    "21-2345-2":3.5,
    "21-1234-3":3.8,
    "21-4321-1":3.1
}
print(type(cgpa))
print(cgpa)
print(cgpa["21-1234-3"])

# %%
family={
    1:"Richard",
    2:"Florence",
    3:"Jonathan"
}
print(family)
family[10]="Jenny"
family[3]="Aaron"
print(family)

# %%
for k,v in cgpa.items():
    print(k,v)

# %%
for k in cgpa.keys():
    print(k)

# %%
for v in cgpa.values():
    print(v)

# %%
for k in cgpa.keys():
    print(k,cgpa[k])

# %%
quiz={}
quiz["21-2345-2"]=20
quiz["21-1234-3"]=15
quiz["21-5678-3"]=10
print(quiz)
quiz["21-5678-3"]=14
print(quiz)

# %%
marks={}
f=open("quiz.txt","r")

for i in range(3):
    line=f.readline()
    s_line=line.split()
    id=s_line[0]
    marks[id]=[]
    mark1=int(s_line[1])
    mark2=int(s_line[2])
    marks[id].append(mark1)
    marks[id].append(mark2)

print(marks)
marks["21-2345-2"].append(22)
print(marks)
f.close()
# split


# %%
marks={}
f=open("1.txt","r")

for i in range(3):
    line=f.readline()
    s_line=line.split()
    id=s_line[0]
    marks[id]=[]
    
print(marks)
marks["21-2345-2"].append(22)
marks["21-2345-2"].append(20)
print(marks)
f.close()
# split


# %%
def createList(n):
    m={}
    for i in range(n):
        m[i]=[]
    return m

f=open("graph.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
print(n,m)

G=createList(n)
print(G)
for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u].append(v)
f.close()
print(G)

# %% [markdown]
# # graph input

# %%


# %% [markdown]
# # graph using adjacency Matrix

# %%


# %% [markdown]
# # graph using adjacency List

# %%
def createList(n):
    m={}
    for i in range(n):
        m[i]=[]
    return m

f=open("g1.txt","r")
vertex_edges=f.readline()
n_m=vertex_edges.split()
n=int(n_m[0])
m=int(n_m[1])
print(n,m)

G=createList(n)
for i in range(m):
    line=f.readline()
    u_v=line.split()
    u=int(u_v[0])
    v=int(u_v[1])
    G[u].append(v)
    G[v].append(u)
f.close()
print(G)

# %%



