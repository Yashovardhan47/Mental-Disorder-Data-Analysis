import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Disorder': ['Anxiety', 'Depression', 'Bipolar', 'Anxiety', 'Depression', 'Bipolar'],
    'Symptom_Severity': [7, 8, 5, 6, 7, 6],
    'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb']
}

df = pd.DataFrame(data)

grouped = df.groupby(['Disorder', 'Month'])['Symptom_Severity'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=grouped, x='Month', y='Symptom_Severity', hue='Disorder')
plt.title('Average Symptom Severity by Disorder and Month')
plt.ylabel('Average Symptom Severity')
plt.xlabel('Month')
plt.legend(title='Disorder')
plt.show()
