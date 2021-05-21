import numpy as np

x = 100
y = np.log(1 + x ** 2) * (1/(np.e * np.sin(x)+1))/(5/4 + 1/(x ** 15))
print(y)
