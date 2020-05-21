import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#read the csv to a pandas dataframe.
df = pd.read_csv('WorldCupMatches.csv')
#Sum of all goals per game.
df['Total_Goals'] = df['Home Team Goals'] \
+ df['Away Team Goals']
print(df.head())
#Goals scored each year.
df1 = df.groupby('Year').Total_Goals \
.apply(lambda x: sum(x)).reset_index()
print(df1.head())
#visualize the goals scored each year.
fig, ax = plt.subplots(figsize = (12,7))
sns.set_style('whitegrid')
sns.set_context('poster')
sns.barplot(data = df1, x = 'Year', y = 'Total_Goals')
plt.xticks(rotation = 45)
ax.set_title('Goals scores in the world cup each year(1930-2014)')
plt.show()
#Load the goals csv into pandas dataframe
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
#A box plot to visualize the distribution of goals
fig, ax1 = plt.subplots(figsize = (12,7))
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale = 1.25)
sns.set_palette('spectral')
sns.boxplot(
  data = df_goals, x = 'home/away', y = 'goals'
)
ax1.set_title("Box distribution for Home Teams' Goals")
plt.show()