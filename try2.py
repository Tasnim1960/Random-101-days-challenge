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