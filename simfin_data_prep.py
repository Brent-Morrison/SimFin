# Imports
import pandas as pd

file_loc = 'C:/Users/brent/simfin_data/'

industries = pd.read_csv(file_loc + 'industries.csv', sep = ';', index_col = 0)
us_companies = pd.read_csv(file_loc + 'us-companies.csv', sep = ';', index_col = 0)
us_balance_sheet = pd.read_csv(file_loc + 'us-balance-quarterly.csv', sep = ';', index_col = 0)
us_income_statement = pd.read_csv(file_loc + 'us-income-quarterly.csv', sep = ';', index_col = 0)
us_cashflow = pd.read_csv(file_loc + 'us-cashflow-quarterly.csv', sep = ';', index_col = 0)
us_shareprices = pd.read_csv(file_loc + 'us-shareprices-daily.csv', sep = ';', index_col = 0)

# Extract for test
orcl_price = us_shareprices.loc['ORCL']
orcl_bs = us_balance_sheet.loc['ORCL']
adp_bs = us_balance_sheet.loc['ADP']

print(us_income_statement.loc['MSFT', [REVENUE, NET_INCOME]])