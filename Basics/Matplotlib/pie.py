import matplotlib.pyplot as plt
from matplotlib import style;

#Styling
print(style.available)
style.use('dark_background')

#Coordinates
products = ['detergent','sweets','water']
sales = [10,20,40]
color = ['purple','orange','blue']

plt.pie(sales,labels=products, colors=color)
plt.show()

