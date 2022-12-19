import matplotlib.pyplot as plt
import numpy as np
x = ["A","B","C","D","E"]
y = np.array([1,2,3,4,5])
plt.pie(y,labels = x)
plt.show()