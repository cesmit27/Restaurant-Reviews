import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'D:\WebScraper\Restaurant_Data_Scraped.csv')
print(df.columns)

plot = sns.catplot(
    data=df, x="rating", y="num_ratings",
    kind="swarm", col="type", aspect=0.7,
)
plot.set_axis_labels('Rating', 'Number of Ratings')
plt.show()
