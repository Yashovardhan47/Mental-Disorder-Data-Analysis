 import pandas as pd
 import matplotlib.pyplot as plt
 data = {
 'Disorder': ['Anxiety', 'Depression', 'Anxiety', 'PTSD', 'Depression', 'Bipolar',
 'PTSD', 'Bipolar', 'Anxiety'],
 'Value': [3.5, 4.2, 2.8, 5.0, 3.7, 4.8, 4.1, 5.2, 3.0]
 }
 df = pd.DataFrame(data)
 average_values = df.groupby('Disorder')['Value'].mean()
 print("Unique disorders and their average values:\n", average_values)
 plt.figure(figsize=(10, 6))
 average_values.plot(kind='bar', color='skyblue', edgecolor='black')
 plt.title('Average Value for Each Disorder')
 plt.xlabel('Disorder')
 plt.ylabel('Average Value')
 plt.xticks(rotation=45)
 plt.show()
