#!/usr/bin/python
# -*- coding: utf-8 -*-

# Acesso a API

import requests, time
from urllib import urlencode

class ApiAccessClass():
    def __init__(self):
        self.__ApiKey       = '68c9346c5d9b4f41b4d975c3b1928e69'
        self.__URL          = 'https://bittrex.com/api/v1.1/'
        self.__marketList   = ['selllimit', 'cancel', 'buylimit','getopenorders']

    def getAPI(self, command, currency='None', quantity=0, rate=0, uuid='None'):
        ##url = self.__API
        ##url = url.format(self.__URL[self.__API])

        url = self.__URL

        if command in self.__marketList:
            nonce = str(int(time.time() * 1000))
            url = url + 'market/' + command + '?'
            url = url + 'apikey=' + self.__ApiKey
            url = url + '&nonce=' + nonce
            if command == 'selllimit' or command == 'buylimit':
                url = url + '&market=' + currency
                url = url + '&quantity=' + str(quantity)
                url = url + '&rate=' + str(rate)
            elif command == 'cancel':
                url = url + '&uuid=' + uuid
            elif command == 'getopenorders':
                url = url + '&market=' + currency
                


        return url
        
