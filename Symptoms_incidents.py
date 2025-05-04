import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Disorder': ['Anxiety', 'Depression', 'Anxiety', 'PTSD', 'Depression', 'Bipolar',
                 'PTSD', 'Bipolar', 'Anxiety'],
    'Incidents': [50, 70, 30, 45, 60, 20, 35, 25, 40]
}

df = pd.DataFrame(data)

incident_sums = df.groupby('Disorder')['Incidents'].sum()
print("Sum of incidents for each disorder:\n", incident_sums)

plt.figure(figsize=(10, 6))
incident_sums.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('Sum of Incidents for Various Mental Health Disorders')
plt.xlabel('Disorder')
plt.ylabel('Total Incidents')
plt.xticks(rotation=45)
plt.show()
