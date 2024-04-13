import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


df = pd.read_csv(r'D:\WebScraper\Restaurant_Data_Scraped.csv')
# print(df.columns) I was having an issue so I needed to see how it was reading the coumns of my CSV file

bins = [1, 2, 3, 3.3, 3.4, 3.7, 4, 4.5, 5]
labels = [f"{bin_start}-{bins[i+1]}" for i, bin_start in enumerate(bins[:-1])]
df['rating_bins'] = pd.cut(df['rating'], bins=bins, labels=labels, include_lowest=True)

#Sets the color of the bar to it's rating
palette = sns.color_palette('rainbow_r', as_cmap=True)
norm = plt.Normalize(df['rating'].min(), df['rating'].max())
colors = palette(norm(df['rating']))

plot = sns.catplot(
    data=df, kind="bar", x="rating", y="restaurant_name", palette = colors, linewidth = 1, edgecolor ='black'
)
plot.set(xlim=(0, 5))
plot.set_axis_labels('Rating','Restaurant')
plt.show()
plt.savefig('RestuarantGraph.svg')
