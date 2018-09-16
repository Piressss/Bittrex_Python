#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Market, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os
sys.path.append('./')
from ApiAccessClass import *
from DTOClass import *

class MarketClass():
    def __init__(self, apikey, apisecret):
        self.__apiAccess = ApiAccessClass(apikey, apisecret) 
    
    def cancelOrder(self, currency):
        api = self.__apiAccess.getAPI('cancel', currency)
        success = api.get(u'success')
        if success == True:
            return True
        else:
            return False
    
    def buyOrder(self, currency, quantity, rate):
        api = self.__apiAccess.getAPI('buylimit', currency, quantity, rate)
        success = api.get(u'success')
        if success == True:
            return True
        else:
            return False
    
    def sellOrder(self, currency, quantity, rate):
        api = self.__apiAccess.getAPI('selllimit', currency, quantity, rate)
        success = api.get(u'success')
        if success == True:
            return True
        else:
            return False
    
    def getOpenOrders(self, currency):
        data = OrderData()
        api = self.__apiAccess.getAPI('getopenorders', currency)
        success = api.get(u'success')
        if success == True:
            result  = api[u'result']
            if len(result) > 0:
                data._OrderUuid         = result[0].get(u'OrderUuid') 
                data._Currency          = result[0].get(u'Exchange')
                data._OrderType         = result[0].get(u'OrderType')
                data._Quantity          = result[0].get(u'Quantity')
                data._QuantityRemaining = result[0].get(u'QuantityRemaining')
                data._Limit             = result[0].get(u'Limit')
                data._Price             = result[0].get(u'Price')
            data._NumOrders         = len(result)
            return data
        else:
            return 'Null'
    
