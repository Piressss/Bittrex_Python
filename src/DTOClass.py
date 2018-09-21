#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

# CLASS DTO

# Dados de Balanço de uma Moeda
class CurrencyBalanceDataClass:
    def __init__(self):
        self._Currency  = 'Null'
        self._Balance   = 0.00
        self._Available = 0.00
        self._Pending   = 0.00

# Dados de uma moeda
class CurrencyData:
    def __init__(self):
        self._MarketName = 'Null'
        self._High       = 0.00
        self._Low        = 0.00
        self._Volume     = 0.00
        self._Last       = 0.00
        self._BaseVolume = 0.00
        self._Bid        = 0.00
        self._Ask        = 0.00
        self._OpenBuyOrders = 0
        self._OpenSellOrders = 0

# Dados de Livro de Ordens
class OrderBookData:
    def __init__(self):
        self._BuyQuantity    = 10*[0.00]
        self._BuyRate        = 10*[0.00]
        self._SellQuantity   = 10*[0.00]
        self._SellRate       = 10*[0.00]

# Dados do Historico de uma moeda
class CurrencyHistoryData:
    def __init__(self):
        self._Time           = 100*[datetime.now()]
        self._Quantity       = 100*[0.00]
        self._Price          = 100*[0.00]
        self._Total          = 100*[0.00]
        self._FillType       = 100*['Null']
        self._OrderType      = 100*['Null']

# Dados de Ordens
class OrderData:
    def __init__(self):
        self._OrderUuid         = ['Null']
        self._Currency          = ['Null']
        self._OrderType         = ['Null']
        self._Quantity          = 0.00
        self._QuantityRemaining = 0.00
        self._Limit             = 0.00
        self._Price             = 0.00
        self._NumOrders         = 0

# Dados de Analise de Moeda
class CurrencyAnalysisData:
    def __init__(self):
        self._Currency       = 'Null'
        self._Average        = 0.00
        self._Pivot          = 0.00
        self._Res            = [0.00,0.00]
        self._Sup            = [0.00,0.00]
        self._Wr             = 0.00
        self._Rsi            = 0.00
        self._Obv            = 0.00
        self._Volume         = 0.00
        self._Bid            = 0.00
        self._Last           = 0.00
        self._Ask            = 0.00
        self._DayGain        = 0.00

# Dados para Analise dos Candles
class CandleData:
    def __init__(self):
        self._BV            = [] 
        self._Close         = []
        self._High          = []
        self._Low           = []
        self._Open          = []
        self._Volume        = []
