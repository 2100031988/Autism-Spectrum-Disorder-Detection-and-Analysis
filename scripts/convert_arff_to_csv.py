import pandas as pd
from scipy.io import arff

# Load the ARFF file
data = arff.loadarff('data/Autism-Adult-Data.arff')

# Convert to a pandas DataFrame
df = pd.DataFrame(data[0])

# Save the DataFrame as a CSV
df.to_csv('data/autism_data.csv', index=False)

print("Conversion complete. CSV saved as 'data/autism_data.csv'.")
