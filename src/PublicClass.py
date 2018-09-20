#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Publica, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os
sys.path.append('./')
from ApiAccessClass import *
from DTOClass import *

class PublicClass():
    def __init__(self):
        self.__apiAccess = ApiAccessClass() 
   
    def getSummaryCurrency(self, currency):
        data = CurrencyData()
        api = self.__apiAccess.getAPI('getmarketsummary', currency)
        success = api.get(u'success')
        if success == True:
            result  = api[u'result']
            data._MarketName = result[0].get(u'MarketName')
            data._High       = result[0].get(u'High') 
            data._Low        = result[0].get(u'Low') 
            data._Volume     = result[0].get(u'Volume') 
            data._Last       = result[0].get(u'Last') 
            data._BaseVolume = result[0].get(u'BaseVolume') 
            data._Bid        = result[0].get(u'Bid') 
            data._Ask        = result[0].get(u'Ask') 
            data._OpenBuyOrders = result[0].get(u'OpenBuyOrders')
            data._OpenSellOrders = result[0].get(u'OpenSellOrders')
            return data
        else:
            return 'Null'

    def getValueCurrency(self, currency):
        data = CurrencyData()
        api = self.__apiAccess.getAPI('getticker', currency)
        success = api.get(u'success')
        if success == True:
            result  = api[u'result']
            print dict.keys(result)
            data._MarketName = currency 
            data._Last       = result.get(u'Last') 
            data._Bid        = result.get(u'Bid') 
            data._Ask        = result.get(u'Ask') 
            return data
        else:
            return 'Null'
    
    def getOrderBook(self, currency):
        data = OrderBookData()
        api = self.__apiAccess.getAPI('getorderbook', currency)
        success = api.get(u'success')
        if success == True:
            result  = api[u'result']
            buy  = result.get(u'buy')
            sell = result.get(u'sell')

            if len(buy) > 10:
                range_length = 10
            else:
                range_length = len(buy)
            for i in range(range_length):
                data._BuyQuantity[i] = buy[i].get(u'Quantity')
                data._BuyRate[i]     = buy[i].get(u'Rate')
            
            if len(sell) > 10:
                range_length = 10
            else:
                range_length = len(sell)
            for i in range(range_length):
                data._SellQuantity[i] = sell[i].get(u'Quantity')
                data._SellRate[i]     = sell[i].get(u'Rate')
            return data
        else:
            return 'Null'
    
    def getMarketHistoryCurrency(self, currency):
        data = CurrencyHistoryData()
        api = self.__apiAccess.getAPI('getmarkethistory', currency)
        success = api.get(u'success')
        if success == True:
            result = api[u'result']
            range_length = len(result)
            for i in range(range_length):
                data._Time[i]      = result[i].get(u'TimeStamp')
                data._Quantity[i]  = result[i].get(u'Quantity')
                data._Price[i]     = result[i].get(u'Price')
                data._Total[i]     = result[i].get(u'Total')
                data._FillType[i]  = result[i].get(u'FillType')
                data._OrderType[i] = result[i].get(u'OrderType')
            return data
        else:
            return 'Null'

    def getCandles(self, currency):
        data = CandleData()
        api = self.__apiAccess.getAPI('GetTicks', currency)
        success = api.get(u'success')
        if success == True:
            result = api[u'result']
            range_length = len(result)
            for i in range(range_length):
                data._BV            = result[i].get(u'BV') 
                data._Close         = result[i].get(u'C') 
                data._High          = result[i].get(u'H') 
                data._Low           = result[i].get(u'L') 
                data._Open          = result[i].get(u'O') 
                data._Volume        = result[i].get(u'V') 
            return data
        else:
            return 'Null'
