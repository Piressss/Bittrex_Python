#!/usr/bin/python
# -*- coding: utf-8 -*-

# Esta implementa a funcao de criptografia da chave para acesso ao Bittrex

from Crypto.Cipher import AES
import json, getpass

class ApiKeyClass:
    def __init__(self):
        self.ApiKey     = '68c9346c5d9b4f41b4d975c3b1928e69'
        self.ApiSecret  = 'a6578e5952214d879acf45d8ff54a7fe'
        self.ApiEncrypt = 'Null'

    def Encrypt(self):
        print self.ApiKey
        print self.ApiSecret
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


m=ApiKeyClass()

print m.Encrypt()
