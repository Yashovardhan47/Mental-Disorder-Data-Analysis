 import numpy as np
 import matplotlib.pyplot as plt
 np.random.seed(0)
 population_size = 1000
 age_mean = 35
 age_std_dev = 15
 ages = np.random.normal(loc=age_mean, scale=age_std_dev,
 size=population_size)
 ages = np.clip(ages, 0, 100)
 plt.figure(figsize=(10, 6))
 plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
 plt.title('Age Profile Distribution')
 plt.xlabel('Age')
 plt.ylabel('Frequency')
 plt.show()

