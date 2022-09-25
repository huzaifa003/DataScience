import matplotlib.pyplot as plt
from matplotlib import style;

#Styling
print(style.available)
style.use('dark_background')

#Coordinates
x1 = [2,3,4]
y1 = [5,6,7]

x2 = [6,7,8]
y2 = [7,10,12]

#Plotting of Coordinates
plt.bar(x1,y1)
plt.bar(x2,y2)

#Lables and titles 
plt.title('testing')
plt.xlabel('X Labels')
plt.ylabel('Y Label')
plt.show()

