# -*- coding: utf-8 -*-
"""
Created on Dec 21 2023

"""
import alpaca_trade_api as tradeapi
import os

api = tradeapi.REST(
    os.environ['PAPER_ACPA_API_KEY_ID'],
    os.environ['PAPER_ACPA_API_SECRET_ID'],
    'https://paper-api.alpaca.markets' #if doing live trades, you want to use 'https://api.alpaca.markets'
)

account = api.get_account()
api.cancel_all_orders()