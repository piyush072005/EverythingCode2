import matplotlib.pyplot as plt
x=[10, 20, 30, 40]
y=['A', 'B', 'C', 'D']
plt.pie(x, labels=y, startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()