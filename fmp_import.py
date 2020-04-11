# Imports
import numpy as np
import pandas as pd
import requests
import json

# References
# https://stackoverflow.com/questions/53558837/python-loop-to-pull-api-data-for-iterating-urls


# Test implementation
ticker_list = 'ABM' #['ORCL', 'ABM', 'ALJJ', 'TRN']
url = 'https://fmpcloud.io/api/v3/'
report = 'balance-sheet-statement/'
apikey = '96a549a2823d1e4a3a66379d2868f0ec'

#r = requests.get(url + report + ticker_list + ?period=quarter&apikey=96a549a2823d1e4a3a66379d2868f0ec')
r = requests.get('https://fmpcloud.io/api/v3/balance-sheet-statement/TRN?period=quarter&apikey=96a549a2823d1e4a3a66379d2868f0ec')

df = pd.read_json(json.dumps(r.json()))

obj = r.json()
print(r.status_code)
print(r == None)
print(r.json())
print(r.json() == None)

if len(r.json()) != 0:









# Looped implementation
ticker_list = ['ORCL', 'ABM', 'ALJJ', 'TRN']
result = None

for ticker in ticker_list:
    r = requests.get('https://fmpcloud.io/api/v3/balance-sheet-statement/{}?period=quarter&apikey=96a549a2823d1e4a3a66379d2868f0ec'.format(ticker))
    if len(r.json()) != 0:
        r_df = pd.read_json(json.dumps(r.json()))
        if result is None:
            result = r_df
        else:
            result = np.concatenate((result, r_df))

print(r.url)
