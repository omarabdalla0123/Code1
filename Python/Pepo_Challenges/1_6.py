import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

List = []
for i in range(80000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    total = dice1 + dice2 + dice3
    List.append(total)

di = {}
for value in List:
    if value not in di:
        di[value] = 0
    di[value] += 1

keys = np.array(sorted(di.keys()))
values = np.array([di[k] for k in keys])

# Create smooth curve
x_smooth = np.linspace(keys.min(), keys.max(), 300)
spline = make_interp_spline(keys, values, k=3)  # k=3 = cubic smooth
y_smooth = spline(x_smooth)

plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, color='steelblue', linewidth=2.5)
plt.fill_between(x_smooth, y_smooth, alpha=0.2, color='steelblue')  # shaded area
plt.scatter(keys, values, color='steelblue', zorder=5)              # original points

plt.xlabel('Dice Sum', fontsize=13)
plt.ylabel('Frequency', fontsize=13)
plt.title('Dice Roll Sum Frequency (10,000 rolls)', fontsize=15)
plt.xticks(keys)
plt.tight_layout()
plt.show()