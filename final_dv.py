import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('shopping_trends.csv')

gender_transactions = df['Gender'].value_counts()
gender_transactions.plot(kind='bar', figsize=(10, 6))
plt.title('Number of Transactions by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Transactions')
plt.show()

top_selling = df.groupby('Category')['Item Purchased'].value_counts().groupby(level=0).nlargest(1).reset_index(level=0, drop=True)
top_selling.plot(kind='bar')
plt.xlabel('Category and Product')
plt.ylabel('Count')
plt.title('Top Selling Product in Each Category')
plt.show()


df['Location'].value_counts().plot(kind='bar')
plt.show()

sns.countplot(x='Season', hue='Category', data=df)
plt.show()

color_size = df.groupby(['Color', 'Size']).size().reset_index(name='Count')
max_index = color_size['Count'].idxmax()
popular_combination = color_size.loc[max_index, ['Color', 'Size']]
print(f'Most popular color and size combination: {popular_combination["Color"]} and {popular_combination["Size"]}')

# For visualization, we plot the top 10 combinations
top_combinations = color_size.nlargest(10, 'Count')
top_combinations.set_index(['Color', 'Size'], inplace=True)
top_combinations.plot(kind='bar')
plt.xlabel('Color and Size')
plt.ylabel('Count')
plt.title('Top 10 Popular Color and Size Combinations')
plt.show()


df.groupby('Location')['Age'].mean().plot(kind='bar')
plt.show()

df.groupby('Payment Method')['Purchase Amount (USD)'].sum().plot(kind='bar')
plt.show()

df['Item Purchased'].value_counts().nlargest(10).plot(kind='bar')
plt.show()

df['Age'].value_counts().nlargest(10).plot(kind='bar')
plt.show()

df['Log Purchase Amount'] = np.log(df['Purchase Amount (USD)'])
df['Log Previous Purchases'] = np.log(df['Previous Purchases'])
sns.scatterplot(x='Log Purchase Amount', y='Log Previous Purchases', data=df, alpha=0.3)
plt.show()


sns.boxplot(x='Category', y='Age', data=df)
plt.show()

