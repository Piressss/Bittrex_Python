#!/usr/bin/python
# -*- coding: utf-8 -*-

# Acesso a API

import json, getpass, hmac, hashlib
import requests, time
from urllib import urlencode
from Crypto.Cipher import AES

class ApiAccessClass():
    def __init__(self):
        self.__URL          = 'https://bittrex.com/api/v1.1/'
        self.__marketList   = ['selllimit', 'cancel', 'buylimit','getopenorders']
        self.__publicList   = ['getmarketsummary', 'getticker', 'getorderbook', 'getmarkethistory']
        self.__accountList  = ['getbalance', 'getorderhistory']
        self.__ApiKey       = '68c9346c5d9b4f41b4d975c3b1928e69'
        self.__ApiSecret    = 'a6578e5952214d879acf45d8ff54a7fe'
        self.__ApiEncrypt   = 'Null'

    def getAPI(self, command, currency='None', quantity=0, rate=0, uuid='None'):
        url = self.__URL
       
        # Public API
        if command in self.__publicList:
            url = url + 'public/' + command + '?'
            url = url + 'market=' + currency  
            if command == 'getorderbook':
                url = url + '&type=both'
            response = self.execRequest(url, 'none')
        # Market API
        elif command in self.__marketList:
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
            # encriptando a url
            sign = self.Encrypt(url)
            response = self.execRequest(url, sign)
        # Account API
        elif command in self.__accountList:
            nonce = str(int(time.time() * 1000))
            url = url + 'account/' + command + '?'
            url = url + 'apikey=' + self.__ApiKey
            url = url + '&nonce=' + nonce
            if command == 'getbalance':
                currency = currency.split('-')
                url = url + '&currency=' + currency[1]
            print url
            sign = self.Encrypt(url)
            response = self.execRequest(url, sign)

        return response
                
    # Utilizado para desencriptar o dado recebido do get feito para a api
    def Encrypt(self, url):
        sign = hmac.new(self.__ApiSecret.encode(), url.encode(), hashlib.sha512).hexdigest()
        return sign
    
    # Request Url
    def execRequest(self, url, sign):
        return requests.get(url, headers = {'apisign': sign}, timeout = 10).json()
        
