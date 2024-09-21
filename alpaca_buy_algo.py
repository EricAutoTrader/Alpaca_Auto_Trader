# -*- coding: utf-8 -*-
"""
Created on Dec 21 2023

"""
import alpaca_trade_api as tradeapi
import math
import requests
import json
import os
import time

def alpaca_custom_buy_order_market(api, symbol, est_value):
    ask = api.get_latest_quote(symbol)._raw['ap']
    qty = math.floor(est_value / ask)
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='day',
    )
    return None

def alpaca_custom_buy_order_limit(api, symbol, est_value):
    ask = api.get_latest_quote(symbol)._raw['ap']
    bid = api.get_latest_quote(symbol)._raw['bp']
    mid = (bid + ask) / 2
    mid = round(mid, 2)
    qty = math.floor(est_value / mid)
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        time_in_force='day',
        limit_price=mid,
        extended_hours = True
    )
    return None

def alpaca_custom_stop_sell(api, symbol, qty, stop_price, stop_limit):
    return_code = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='stop_limit',
        time_in_force='day',
        stop_price =  stop_price,
        limit_price = stop_limit
#        stop_loss={'stop_price': round((stop_price * 1.1),2), 'limit_price': round((stop_limit * 1.11),2)}
        )
    return return_code

#Instantiate Alpaca API session.  
api = tradeapi.REST(
    os.environ['PAPER_ACPA_API_KEY_ID'],
    os.environ['PAPER_ACPA_API_SECRET_ID'],
    'https://paper-api.alpaca.markets' #if doing live trades, you want to use 'https://api.alpaca.markets'
)
#Obtain existing account and positions info from Alpaca
portfolio = api.list_positions()
list_positions = []
for position in portfolio:
    list_positions.append(position.symbol)
account = api.get_account()

#Get recommended buys.  This can come from any buy signal provider. Algo10.com has a good track record
print("*********************  getting buy recommendations based on Technical Analysis ***********")
url = "https://data.algo10.com/buys_json.html"
response = requests.get(url, auth=('username', 'password'))
recommendation_list = json.loads(response.text)

#Execute buy orders
print("*********************  Buying assets ***********")
est_value = float(account.non_marginable_buying_power) / len(recommendation_list)
#est_value = float(account.buying_power) / len(recommendation_list) You can also choose to use margin 
for ticker in recommendation_list:
    if ticker not in list_positions:
        try:
            print(alpaca_custom_buy_order_limit(api, ticker, est_value))
            print(f"success buying {ticker}")
        except:
            print(f"error buying {ticker}")
    else:
        print("already in portfolio")

#give 2 seconds for everything to settle
print("*********************  Done buying assets  ***********")
time.sleep(2)

#If there are any tickers you want to keep, you can customize this by adding tickers like follows: 
# hold_positions = ['SPY', 'RSP', 'SHY', 'TLT', 'IWM', 'IJR', 'DJD', 'QQQ']
hold_positions = []

print("*********************  Setting stop losses ***********")
for position in portfolio:
    if position.symbol not in hold_positions:
        try:
            print(position.symbol)
            print(float(position.avg_entry_price) )
            stop_price = round((float(position.avg_entry_price) * .99), 2)
            stop_limit = round((float(position.avg_entry_price) * .985), 2)
            print(stop_limit)
            print(stop_price)
            buy_price = alpaca_custom_stop_sell(api, position.symbol, int(position.qty), stop_price, stop_limit)
            print (buy_price)
        except Exception as e: 
            print(f"error stopping {position.symbol} because of {e}")

print("*********************  Done setting stop losses  ***********")

