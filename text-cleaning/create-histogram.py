import pandas as pd
import matplotlib.pyplot as plt

file_path = "news-articles-data.xlsx"

df = pd.read_excel(file_path)

# Check the structure of your DataFrame
print(df.head())

# Create a bar plot to visualize the number of articles published in each year
plt.figure(figsize=(10, 6))
df['Year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Number of Articles Published Each Year (1987-1998)')
plt.xlabel('Year')
plt.ylabel('Number of Articles')
plt.show()