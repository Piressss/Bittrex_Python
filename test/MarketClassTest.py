#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from MarketClass import *
from DTOClass import *

# Must enter with the key and secret key before run
key     ='Null'
secret  ='Null'

if key == 'Null':
    print 'Must enter with the key and secret key before run'
    exit(0)
elif secret == 'Null':
    print 'Must enter with the key and secret key before run'
    exit(0)

c = MarketClass(key, secret)

a = c.getOpenOrders('BTC-SRN')
print a._NumOrders
print "\n"
