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

