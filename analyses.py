# I'll simulate a sample dataframe since I don't have access to the original data.
# This will help illustrate the concept.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sample_size = 100

# Generate random data for demonstration
df_sample = pd.DataFrame({
    'n_bars': np.random.randint(1000, 1500, sample_size),
    'n_beats': np.random.randint(4000, 6000, sample_size)
})

# Filter the dataframe for rows where n_bars is greater than 1200
filtered_df = df_sample[df_sample['n_bars'] > 1200]

# Plot the scatter plot
plt.scatter(filtered_df['n_bars'], filtered_df['n_beats'])
plt.xlabel('n_bars')
plt.ylabel('n_beats')
plt.show()
