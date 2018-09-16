#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Account, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os
sys.path.append('./')
from ApiAccessClass import *
from DTOClass import *

class AccountClass():
    def __init__(self, apikey, apisecret):
        self.__apiAccess = ApiAccessClass(apikey, apisecret) 

    def getCurrencyBalance(self, currency):
        data = CurrencyBalanceDataClass()
        api = self.__apiAccess.getAPI('getbalance', currency)
        success = api.get(u'success')
        if success == True:
            result  = api[u'result']
            data._Currency      = result.get(u'Currency')
            data._Balance       = result.get(u'Balance')
            data._Available     = result.get(u'Available')
            data._Pending       = result.get(u'Pending')
            return data
        else:
            return 'Null'
    
    def getOrderHistory(self, currency):
        data = OrderData()
        api = self.__apiAccess.getAPI('getorderhistory')
        success = api.get(u'success')
        print api
        if success == True:
            result  = api[u'result']
            if len(result) != 0 :
                data._OrderUuid     = result.get(u'OrderUuid')
                data._Currency      = result.get(u'Exchange')
                data._OrderType     = result.get(u'OrderType')
                data._Quantity      = result.get(u'Quantity')
                data._QuantityRemaining = result.get(u'QuantityRemaining')
                data._Limit         = result.get(u'Limit')
                data._Price         = result.get(u'Price')
                data._NumOrders     = 1
            return data
        else:
            return 'Null'
