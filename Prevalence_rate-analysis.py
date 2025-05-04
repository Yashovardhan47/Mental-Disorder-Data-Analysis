import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Disorder': ['Anxiety', 'Depression', 'Anxiety', 'PTSD', 'Depression', 'Bipolar',
                 'PTSD', 'Bipolar', 'Anxiety'],
    'Incidents': [50, 70, 30, 45, 60, 20, 35, 25, 40]
}

df = pd.DataFrame(data)

grouped_data = df.groupby('Disorder').agg(
    Total_Incidents=('Incidents', 'sum'),
    Count=('Incidents', 'count')
)

grouped_data['Prevalence'] = grouped_data['Total_Incidents'] / grouped_data['Count']

print("Prevalence of each disorder:\n", grouped_data['Prevalence'])

plt.figure(figsize=(10, 6))
grouped_data['Prevalence'].plot(kind='bar', color='teal', edgecolor='black')
plt.title('Prevalence of Each Disorder')
plt.xlabel('Disorder')
plt.ylabel('Prevalence (Average Incidents per Record)')
plt.xticks(rotation=45)
plt.show()
