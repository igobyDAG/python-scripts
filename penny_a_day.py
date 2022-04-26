from matplotlib import pyplot as plt

def double_penny(days):
    return 2**(days-1) * 0.01

growth = []

for i in range(30):
    growth.append(double_penny(i))


print(growth)
plt.plot(growth)
plt.show()