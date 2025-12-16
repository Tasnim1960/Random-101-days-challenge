# --- 1. ADJACENCY MATRIX ---
def createMatrix(n):
    m = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0) 
        m.append(r)
    return m

def printMatrix(m):
    for r in m:
        print(r)

print("--- Weighted Adjacency Matrix ---")
f = open("graph.txt", "r")
vertex_edges = f.readline()
n_m = vertex_edges.split()
n = int(n_m[0])
m = int(n_m[1])
print("Vertices:", n, "Edges:", m)

G = createMatrix(n)

for i in range(m):
    line = f.readline()
    u_v_w = line.split()
    u = int(u_v_w[0])
    v = int(u_v_w[1])
    w = int(u_v_w[2])
    
    # Directed Graph: Only set u -> v
    G[u][v] = w 

printMatrix(G)
f.close()


# --- 2. ADJACENCY LIST ---
def createList(n):
    l = {}
    for i in range(n):
        l[i]=[] 
    return l



print("\n--- Weighted Adjacency List ---")
f = open("graph.txt", "r")
vertex_edges = f.readline()
n_m = vertex_edges.split()
n = int(n_m[0])
m = int(n_m[1])
print(n,m)

G= createList(n)

for i in range(m):
    line = f.readline()
    u_v_w = line.split()
    u = int(u_v_w[0])
    v = int(u_v_w[1])
    w = int(u_v_w[2])
    
    # Directed Graph: Append [v, w] to u's list
    G[u].append([v, w])

print(G)
f.close()


