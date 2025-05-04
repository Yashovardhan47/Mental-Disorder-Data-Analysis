import pandas as pd
 import matplotlib.pyplot as plt
 data = {
 'Disorder': ['Anxiety', 'Depression', 'Anxiety', 'PTSD', 'Depression', 'Bipolar',
 'PTSD', 'Bipolar', 'Anxiety'],
 'Incidents': [50, 70, 30, 45, 60, 20, 35, 25, 40]
 }
 df = pd.DataFrame(data)
 total_incidents = df.groupby('Disorder')['Incidents'].sum()
 print("Total incidences for each diagnosed disorder:\n", total_incidents)
 plt.figure(figsize=(10, 6))
 total_incidents.plot(kind='bar', color='cornflowerblue', edgecolor='black')
 plt.title('Total Incidences of Each Diagnosed Disorder')
 plt.xlabel('Disorder')
 plt.ylabel('Total Incidences')
 plt.xticks(rotation=45)
 plt.show()
