import matplotlib.pyplot as plt

# ----- Data -----
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 7, 4]

# ----- Line Graph -----
plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# ----- Bar Graph -----
plt.figure(figsize=(6,4))
plt.bar(x, y)
plt.title("Simple Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ----- Scatter Plot -----
plt.figure(figsize=(6,4))
plt.scatter(x, y)
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
