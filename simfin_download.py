# Simfin download script

# !pip install simfin

import simfin as sf

# Set your API-key for downloading data. This key gets the free data.
sf.set_api_key('free')

# Set the local directory where data-files are stored.
# The directory will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Download the data from the SimFin server and load into a Pandas DataFrame.
df = sf.load_balance(variant='quarterly', market='us')

# Print the first rows of the data.
print(df.head())
