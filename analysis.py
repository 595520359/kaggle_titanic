import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

carrier_count = train_data["Pclass"].value_counts()
sns.set(style="darkgrid")
# sns.barplot(carrier_count.index, carrier_count.values, alpha=0.9)
sns.barplot(data=carrier_count, alpha=0.9)
plt.title('Frequency Distribution of pclass')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('pclass', fontsize=12)
plt.show()

train_data["Pclass"].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8)).legend()
