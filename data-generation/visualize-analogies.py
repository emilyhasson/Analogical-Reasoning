import pandas as pd
import matplotlib.pyplot as plt

dates_path = "../text-cleaning/news-articles-data.xlsx"
analogies_path = "filtered-user-responses-positive.xlsx"

df1 = pd.read_excel(dates_path)
df2 = pd.read_excel(analogies_path)

# df2 = df2.drop_duplicates(subset=['FILE'], keep='first')

df3 = pd.merge(df1, df2, left_on='Name', right_on='FILE', how='inner')
df3 = df3.drop(columns=['FILE'])


# Assuming df3 has a column named "Year"
year_counts = df3['Year'].value_counts()

# Print the counts
# print("Count of rows for each year (positive hit):")
# print(year_counts)

# Visualize the counts
# plt.figure(figsize=(10, 6))
# year_counts.plot(kind='bar', color='skyblue')
# plt.title('Count of Rows for Each Year')
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.show()

year_counts_totals = df1['Year'].value_counts()
# print("Count of rows for each year (totals):")
# print(year_counts_totals)


# Combine positive_hits and totals into a single DataFrame
ratios_df = pd.DataFrame({'Positive Hits': year_counts, 'Totals': year_counts_totals})

# Fill NaN values with 0 for years not present in either Series
ratios_df = ratios_df.fillna(0)

# Calculate the ratio of Positive Hits to Totals
ratios_df['Ratio'] = ratios_df['Positive Hits'] / ratios_df['Totals']

# Print the resulting DataFrame
# print("Ratios of Positive Hits to Totals for each year:")
# print(ratios_df)

# Plotting the ratios
plt.figure(figsize=(10, 6))
plt.bar(ratios_df.index, ratios_df['Ratio'], color='skyblue')
plt.title('Ratios of Analogies to Total Articles for Each Year')
plt.xlabel('Year')
plt.ylabel('Ratio')
plt.xticks(rotation=45)
plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Assuming ratios_df is a DataFrame
# # Make sure to run the previous code to create the ratios_df DataFrame

# # Function to calculate ratio and perform bootstrapping
# def calculate_ratio_with_bootstrap(data):
#     ratios = []
#     for _ in range(num_samples):
#         # Resample with replacement
#         sample = data.sample(n=len(data), replace=True)
#         # Calculate ratio for the resampled data
#         ratio = sample['Positive Hits'].sum() / sample['Totals'].sum()
#         ratios.append(ratio)
#     return ratios

# # Number of bootstrap samples
# num_samples = 1000

# # Calculate ratios and confidence intervals
# ratios_df['Confidence Intervals'] = ratios_df.apply(lambda row: np.percentile(calculate_ratio_with_bootstrap(ratios_df), [2.5, 97.5]), axis=1)

# # Plotting the ratios with confidence intervals
# plt.errorbar(
#     ratios_df.index,
#     ratios_df['Ratio'],
#     yerr=[
#         np.abs(ratios_df['Ratio'] - ratios_df['Confidence Intervals'].apply(lambda x: x[0])),
#         np.abs(ratios_df['Confidence Intervals'].apply(lambda x: x[1]) - ratios_df['Ratio'])
#     ],
#     fmt='none',
#     ecolor='orange',
#     capsize=5,
#     label='95% Confidence Intervals'
# )


# plt.title('Ratios of Positive Hits to Totals for Each Year with Confidence Intervals')
# plt.xlabel('Year')
# plt.ylabel('Ratio')
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()
