import matplotlib.pyplot as plt
from matplotlib import style;
import numpy as np
#Styling
print(style.available)
style.use('dark_background')

#Coordinates
numbers = np.random.randint(185, size=20)
jump = np.sort(np.random.randint(100,size=8)) #Jump should be increasing

print(numbers)
#Plotting of Coordinates
plt.hist(numbers,jump,histtype='bar')

#Lables and titles 
plt.title('testing')
plt.xlabel('X Labels')
plt.ylabel('Y Label')
plt.show()

