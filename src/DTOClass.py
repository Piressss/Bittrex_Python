#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

# CLASS DTO

# Dados de Balanço de uma Moeda
class CurrencyBalanceDataClass:
    def __init__(self):
        self.__Currency  = 'Null'
        self.__Balance   = 0.00
        self.__Available = 0.00
        self.__Pending   = 0.00

# Dados de uma moeda
class CurrencyData:
    def __init__(self):
        self.__MarketName = 'Null'
        self.__High       = 0.00
        self.__Low        = 0.00
        self.__Volume     = 0.00
        self.__Last       = 0.00
        self.__BaseVolume = 0.00
        self.__Bid        = 0.00
        self.__Ask        = 0.00
        self.__OpenBuyOrders = 0
        self.__OpenSellOrders = 0

# Dados de Livro de Ordens
class OrderBookData:
    def __init__(self):
        self.__BuyQuantity    = 10*[0.00]
        self.__BuyRate        = 10*[0.00]
        self.__SellQuantity   = 10*[0.00]
        self.__SellRate       = 10*[0.00]

# Dados do Historico de uma moeda
class CurrencyHistoryData:
    def __init__(self):
        self.__Time           = 100*[datetime.now()]
        self.__Quantity       = 100*[0.00]
        self.__Price          = 100*[0.00]
        self.__Total          = 100*[0.00]
        self.__FillType       = 100*['Null']
        self.__OrderType      = 100*['Null']

# Dados de Ordens
class OrderData:
    def __init__(self):
        self.__OrderUuid      = ['Null']
        self.__Currency       = ['Null']
        self.__OrderType      = ['Null']
        self.__Quantity       = 0.00
        self.__Limit          = 0.00
        self.__Price          = 0.00
        self.__NumOrders      = 0

# Dados de Analise de Moeda
class CurrencyAnalysisData:
    def __init__(self):
        self.__Currency       = 'Null'
        self.__Average        = 0.00
        self.__Res            = [0.00,0.00]
        self.__Sup            = [0.00,0.00]
        self.__Wr             = 0.00
        self.__Rsi            = 0.00
        self.__Obv            = 0.00
        self.__Volume         = 0.00
        self.__Bid            = 0.00
        self.__Last           = 0.00
        self.__Ask            = 0.00

