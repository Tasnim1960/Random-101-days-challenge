# %%
print("Please open your notebook")

# %%
list=[10,20,30,40]
print(type(list))
print(list)

# %%
list1=['A',10,20,3.5,"Richard"]
print(list1)

# %%
print(list[0])

# %%
print(len(list))
print(list)

# %%
print(list[len(list)-1])

# %%
print(list[1:3])

# %%
print(list[-1])

# %%
list1=[10]
print(list1)
list1.append(20)
list1.append(30)
list1.append(40)
print(list1)

# %%
x=list1.pop()
print(x)
print(list1)

# %%
list2=[10,20,30,40,50]
list2.pop()
print(list2)

# %%
list2[0]=1000
print(list2)

# %%
list2.reverse()
print(list2)

# %%
list2.sort()
print(list2)

# %%
List1=[]
List1.append(10)
print(List1)

# %%
List1.clear()
print(List1)

# %%
List1=[10,20,30,40,50]
print(len(List1))

# %%
List1.pop(0)
print(List1)

# %%
List1.remove(30)
print(List1)

# %%
List2=[0,10,10,20,30,40]
print(100 in List2)
print(List2)

# %%
t=(10,20,30,40)
print(type(t))
print(t[0])
# Tuple immutable

# %%
chodon=('A','G','C','T')
print(chodon)

# %% [markdown]
# # Operator and Expression
# - Arithmetic Operator: +,-,*,/,%, **
# - Relational operator: >,>=,<,<=,==,!=
# - Logical Operator : and, or, not

# %%
a=10
b=20
print(a-b)
print(a+b)
print(a*b)
print(a/b) # float division
print(13//5) # integer division
print(a%b)
print(a**3) # exponent

# %%
a=[2,3]
b=[10,-5]
r=a[0]*b[0]+a[1]*b[1]
print(r)

# %%
a=10
b=20
print(a>b)
print(a<=b)
print(a!=b)
print(a==b)

# %%
a=10
b=20
c=30
x=(a>b) and (a>c)
print(x)
y=(a<b) or (a==c)
print(y)

r=True
print(not r)

# %% [markdown]
# # conditional Statement

# %%
age=10
if age>=18:
    print("I am adult")
    print("I am another line")
else:
    print("I am not adult")

# %%
marks=80
if marks>=90:
    print("A+")
elif marks>=85 and marks<90:
    print("A")
else:
    print("F")

# %%



