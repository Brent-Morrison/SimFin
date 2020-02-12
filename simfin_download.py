# Simfin download script

# !pip install simfin

import os
import simfin as sf
from simfin.names import *

# Print the default directory?
print(os.path.expanduser('~'))

# Set your API-key for downloading data. This key gets the free data.
sf.set_api_key('free')

# Set the local directory where data-files are stored.
# The directory will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Download the data from the SimFin server and load into a Pandas DataFrame.
df_companies = sf.load_companies(market = 'us')
df_industries = sf.load_industries()
df_income = sf.load_income(variant = 'quarterly', market = 'us')
df_balance = sf.load_balance(variant = 'quarterly', market = 'us')
df_cashflow = sf.load_cashflow(variant = 'quarterly', market = 'us')
df_prices = sf.load_shareprices(variant = 'daily', market = 'us')

# Print the first rows of the data.
print(df_prices.head())