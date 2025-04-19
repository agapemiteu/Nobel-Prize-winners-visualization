import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('nobel.csv')
print(df.head())
print(df.info())
print(df.columns)

#most commonly awarded gender
top_gender = df['sex'].value_counts()
print('Top gender:')
print(top_gender)

#most commonly awarded birth country
top_country= df['birth_country'].value_counts()
print('Top country:')
print(top_country)

#Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
df = pd.read_csv('nobel.csv')
df['usa_born_winner'] = df['birth_country'] == 'United States of America'
df['decade'] = (np.floor(df['year']/10 )*10).astype(int)
decade_ratios = df.groupby('decade', as_index=False)['usa_born_winner'].mean()
max_decade_usa = decade_ratios.loc[decade_ratios['usa_born_winner'].idxmax(), 'decade']
print(max_decade_usa)

sns.relplot(
    data=decade_ratios,
    x='decade',
    y='usa_born_winner',
    kind='line',
    marker='o',
    aspect=1.5
)

# Add labels and title
plt.title('Ratio of US-born Nobel Prize Winners by Decade')
plt.xlabel('Decade')
plt.ylabel('Ratio of US-born Winners')

plt.show()

#Which decade and Nobel Prize category combination had the highest proportion of female laureates?
df['female_winner'] = df['sex'] == 'Female'
df['decade'] = (np.floor(df['year'] / 10) * 10).astype(int)

#group by decade and award category for female winners
female_ratios = df.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

#get highest proportion of female winners
female_max = female_ratios.loc[female_ratios['female_winner'].idxmax()]

#creating dictionary for easy reference
max_female_dict = {female_max['decade']: female_max['category']}

plot = sns.relplot(
    data = female_ratios,
    x='decade',
    y='female_winner', 
    hue = 'category',
    kind='line',
    marker='o',
    height=5
)

plot.set(
    title ='Proportion of Female Nobel Laureates by Decade and Category',
    xlabel ='Decade',
    ylabel='Proportion of Female Winners'
)

#annotate the max point
ax = plot.ax
ax.scatter(
    female_max['decade'],
    female_max['female_winner'],
    color='red',
    s=100,
    zorder=5,
    label='Highest'
)
plot.tight_layout
plt.show()


#find first woman to win a Nobel Prize
female_winners = df[df['female_winner']== True]

#find the row where the year is minimum among female winners
first_female = female_winners[female_winners['year']==female_winners['year'].min()]

# Display the year and category of the first female Nobel Prize winner
first_female_year = first_female['year'].values[0]
first_female_category = first_female['category'].values[0]


#Determine repeat winners
# Count how many times each full name appears in the dataset
winner_counts = df['full_name'].value_counts()

# Filter only those who have won 2 or more times
repeat_winners = winner_counts[winner_counts >= 2]

# Extract just the names into a list
repeats = repeat_winners.index.tolist()

# Output the result
print(repeats)
