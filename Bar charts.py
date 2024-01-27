import matplotlib.pyplot as plt

categories=['A','B','C','D']

values=[25,40,30,20]

plt.bar(categories,values)
plt.title("My Bar Chart")
plt.xlabel("categories")
plt.ylabel("Values")
plt.show()
