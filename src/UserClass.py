#!/usr/bin/python
# -*- coding: utf-8 -*-

# Classe para acesso aos comandos da API Market, solicita o get da Api e 
# formata o resultado para a classe DTO

import sys,os
sys.path.append('./')
from AnalysisClass import *
from PublicClass import *
from MarketClass import *
from AccountClass import *
from DTOClass import *

class UserClass():
    def __init__(self, apikey, apisecret):
        self.__marketClass = MarketClass(apikey, apisecret) 
        self.__analysisClass = AnalysisClass() 

    def getAnalysis(self, currency):
        result = self.__analysisClass.getCurrencyAnalysis(currency,12) 

        print "Currency Analysis - %s" %currency

