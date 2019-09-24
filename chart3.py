import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# sphinx_gallery_thumbnail_number = 2


df = pd.read_csv('DE25.csv')
data2d = df.values

crossover = [0.05, 0.1, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
factor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
error = data2d[:,7]
error = np.reshape(error,(20, 20))



fig, ax = plt.subplots(figsize = (24,24))
im = ax.imshow(error)

# We want to show all ticks...
ax.set_xticks(np.arange(len(crossover)))
ax.set_yticks(np.arange(len(factor)))
# ... and label them with the respective list entries
ax.set_xticklabels(crossover)
ax.set_yticklabels(factor)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(factor)):
    for j in range(len(crossover)):
        text = ax.text(j, i, error[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Error in DB")
fig.savefig('2.png')
plt.show()