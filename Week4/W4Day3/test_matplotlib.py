import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [num**2 for num in x]

plt.plot(x,y,marker='o')
plt.title('Square Numbers')
plt.xlabel('X: Value')
plt.ylabel('Y: Value')


plt.grid(True)
plt.show()


