#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from PublicClass import *
from DTOClass import *

c = PublicClass()

a = c.getSummaryCurrency('BTC-XRP')
print a._MarketName
print "\n"

a = c.getValueCurrency('BTC-XRP')
print a._Last
print "\n"

a = c.getOrderBook('BTC-XRP')
print a._BuyRate
print "\n"

a = c.getMarketHistoryCurrency('BTC-XRP')
print a._Time
print "\n"

a = c.getCandles('BTC-XRP')
print a._Low
print "\n"
