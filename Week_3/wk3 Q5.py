#Josh Flack
#24/8/2020
#barchar graph

import matplotlib.pyplot as plt
from random import randint
import random as ran
import math as ma

rolls = [randint(0,2) for _ in range(0,50001)]

numbers = range(0,1)
counts = [rolls.count(n) for n in numbers]

run_len = 0 # The current run length.
runs = [] # We'll record run lengths here.
for n in rolls:
  if n == 1: # If it's a head...
    run_len += 1 # Add 1 to run length.
  else: # If it's a tail...
    runs.append(run_len) # Add current run length to runs.
    run_len = 0 # Reset run length
runs.append(run_len) # Append length of last run.

res
t = 0
while t < 50000:
    runs.count(n) for n in rolls
    res.append(n)
    print (res)

#print(runs)# Print results.

plt.bar (counts,runs)
plt.show()
