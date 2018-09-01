#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

# CLASS DTO

# Dados de Balanço de uma Moeda
class CurrencyBalanceDataClass:
    def __init__(self):
        self.Currency  = 'Null'
        self.Balance   = 0.00
        self.Available = 0.00
        self.Pending   = 0.00

# Dados de uma moeda
class CurrencyData:
    def __init__(self):
        self.MarketName = 'Null'
        self.High       = 0.00
        self.Low        = 0.00
        self.Volume     = 0.00
        self.Last       = 0.00
        self.BaseVolume = 0.00
        self.Bid        = 0.00
        self.Ask        = 0.00
        self.OpenBuyOrders = 0
        self.OpenSellOrders = 0

# Dados de Livro de Ordens
class OrderBookData:
    def __init__(self):
        self.BuyQuantity    = 10*[0.00]
        self.BuyRate        = 10*[0.00]
        self.SellQuantity   = 10*[0.00]
        self.SellRate       = 10*[0.00]

# Dados do Historico de uma moeda
class CurrencyHistoryData
    def __init__(self):
        self.Time           = 100*[datetime.now()]
        self.Quantity       = 100*[0.00]
        self.Price          = 100*[0.00]
        self.Total          = 100*[0.00]
        self.FillType       = 100*['Null']
        self.OrderType      = 100*['Null']

# Dados de Ordens
class OrderData
    def __init__(self):
        self.OrderUuid      = ['Null']
        self.Currency       = ['Null']
        self.OrderType      = ['Null']
        self.Quantity       = 0.00
        self.Limit          = 0.00
        self.Price          = 0.00
        self.NumOrders      = 0

# Dados de Analise de Moeda
class CurrencyAnalysisData
    def __init__(self):
        self.Currency       = 'Null'
        self.Average        = 0.00
        self.Res            = [0.00,0.00]
        self.Sup            = [0.00,0.00]
        self.Wr             = 0.00
        self.Rsi            = 0.00
        self.Obv            = 0.00
        self.Volume         = 0.00
        self.Bid            = 0.00
        self.Last           = 0.00
        self.Ask            = 0.00

