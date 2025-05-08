import pandas as pd
import matplotlib.pyplot as plt

# Load the data (adjust the path if needed)
df = pd.read_csv('df_br040_mg.csv', sep=';')

# Extract the relevant columns
km = df['km']
proba_fatal = df['proba_fatal']
proba_medium = df['proba_feridos']
proba_light = df['proba_leve']

# Create the figure with two vertically stacked subplots, sharing the x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

# 1) Scatter plot of predicted probabilities along the road
ax1.scatter(km, proba_fatal, label='Fatal', s=10)
ax1.scatter(km, proba_medium, label='Medium', s=10)
ax1.scatter(km, proba_light, label='Light', s=10)
ax1.set_ylabel('Predicted Probability')
ax1.set_title('Accident Severity Probabilities along BR-040')
ax1.legend()

# 2) Histogram showing density of accidents by kilometer marker
ax2.hist(km, bins=50, density=True)
ax2.set_xlabel('Normalized Kilometer Marker')
ax2.set_ylabel('Accident Density')
ax2.set_title('Accident Density along BR-040')

plt.tight_layout()
plt.show()
