
import pandas as pd
import json
from yahoo_fin import stock_info as si
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from azure.eventhub.exceptions import EventHubError
from datetime import datetime
import asyncio

connection_str = '***'
eventhub_name = '***'

test = si.get_quote_data('AMZN')
test_df = pd.DataFrame([test], columns=test.keys())[['regularMarketTime','regularMarketPrice','marketCap','exchange','averageAnalystRating']]
datetime.fromtimestamp(test_df['regularMarketTime'])
test_df['averageAnalystRating'].str.split(' - ', 1, expand=True)
test_df.apply(lambda row: "$" + str(round(row['marketCap']/1000000000000,2)) + 'MM', axis=1)

def get_data_for_stock(stock):
    stock_pull = si.get_quote_data(stock)
    stock_dataframe = pd.DataFrame([stock_pull], columns=stock_pull.keys())[['regularMarketTime','regularMarketPrice','marketCap','exchange','averageAnalystRating']]

    stock_dataframe['regularMarketTime'] = datetime.fromtimestamp(stock_dataframe['regularMarketTime'])
    stock_dataframe['regularMarketTime'] = stock_dataframe['regularMarketTime'].astype(str)
    
    stock_dataframe[['AnalystRating', 'AnalystBuySell']] = stock_dataframe['averageAnalystRating'].str.split(' - ', 1, expand=True)
    
    stock_dataframe.drop('averageAnalystRating', axis=1, inplace=True)

    stock_dataframe['MarketCapInTrills$$'] = stock_dataframe.apply(lambda row: "$" + str(round(row['marketCap']/1000000000000,2)) + 'MM', axis=1)

    return stock_dataframe.to_dict('record')

datetime.now()
get_data_for_stock('AMZN')