#Josh Flack
#22/7/2020
#first random scatter graph

import random
import math
import matplotlib.pyplot as plt

ran1 = list(random.sample(range(0,10),10))
ran2 = list(random.sample(range(0,10),10))

plt.scatter (ran1,ran2)
plt.show()

