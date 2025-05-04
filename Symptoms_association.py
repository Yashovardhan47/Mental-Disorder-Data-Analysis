import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Disorder': ['Anxiety', 'Depression', 'Anxiety', 'PTSD', 'Depression', 'Bipolar',
                 'PTSD', 'Bipolar', 'Anxiety'],
    'Symptoms': ['Fatigue', 'Sadness', 'Nervousness', 'Flashbacks', 'Hopelessness',
                 'Mood swings', 'Nightmares', 'Irritability', 'Restlessness']
}

df = pd.DataFrame(data)

symptom_counts = df.groupby(['Disorder', 'Symptoms']).size().unstack(fill_value=0)

print("Symptoms associated with each disorder:\n", symptom_counts)

symptom_counts.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20')
plt.title('Symptoms Associated with Various Disorders')
plt.xlabel('Disorder')
plt.ylabel('Symptom Frequency')
plt.legend(title='Symptoms', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()
