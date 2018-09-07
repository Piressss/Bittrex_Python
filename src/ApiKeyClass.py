#!/usr/bin/python
# -*- coding: utf-8 -*-

# Esta implementa a funcao de decriptografia da requisicao da API

from Crypto.Cipher import AES
import json, getpass, hmac, hashlib

class ApiKeyClass:
    def __init__(self):
        self.__ApiKey     = '68c9346c5d9b4f41b4d975c3b1928e69'
        self.__ApiSecret  = 'a6578e5952214d879acf45d8ff54a7fe'
        self.__ApiEncrypt = 'Null'

    # Sem uso
    def Encrypt(self):
        export = True
        export_fn = 'secrets,json'
        cipher = AES.new(getpass.getpass('Input encryption password (string will not show)'))
        apikey_enc      = cipher.encrypt(self.ApiKey)
        apisecret_enc   = cipher.encrypt(self.ApiEncrypt)
        api = {'key': str(apikey_enc), 'secret': str(apisecret_enc)}
        if export:
            with open(export_fn, 'w') as outfile:
                json.dump(api, outfile)
        return api

    # Utilizado para desencriptar o dado recebido do get feito para a api
    def Decrypt(self, api_resp):
        apisign = hmac.new(self.ApiSecret.encode(), api_resp.encode(), hashlib.sha512).hexdigest()
        return apisign

     
