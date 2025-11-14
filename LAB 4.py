# %%
print("Welcome to AI Lab4")

# %% [markdown]
# # Library Fucntion
# - Math
# - Random
# - matplotlib
# - numpy
# - panda

# %%
import random
n=random.randint(1,100)
print(n)

# %%
import random
dice=[]
for i in range(100):
    dice.append(random.randint(1,6))
print(dice)
    

# %%
print(random.random())

# %%
gene=""
codom=('A','C','G','T')
for i in range(100):
    gene=gene+random.choice(codom)
print(gene)

# %%
import math
print(math.sqrt(4))

# %%
import matplotlib.pyplot as plt
x=[-3,-2,-1,0,1,2,3]
y=[5,2,1,7,8,10,3]
plt.plot(x,y)
plt.grid()
plt.show()

# %% [markdown]
# # Matrix(List of List)

# %%
m=[
    [1,2,3,4],
    [2,4,6,8],
    [1,3,5,7]
]
print(m)
print(type(m))
print(len(m))
print(m[1])
print(len(m[0]))

# %%
row=3
col=4
m=[]
for i in range(row):
    r=[]
    for j in range(col):
        r.append(0)
    m.append(r)

for r in m:
    print(r)

# %%
def createMatrix(row,col):
    m=[]
    for i in range(row):
        r=[]
        for j in range(col):
            r.append(0)
        m.append(r)
    return m

def printMatrix(m):
    for r in m:
        print(r)

g=createMatrix(10,10)
printMatrix(g)

# %%
def createIdentityMatrix(n):
    m=[]
    for i in range(n):
        r=[]
        for j in range(n):
            if i==j:
                r.append(1)
            else:
                r.append(0)
        m.append(r)
    return m

def printMatrix(m):
    for r in m:
        print(r)

g=createIdentityMatrix(5)
printMatrix(g)

# %%



