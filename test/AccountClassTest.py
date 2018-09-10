#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/')
from AccountClass import *
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

c = AccountClass(key, secret)

a = c.getCurrencyBalance('BTC-SRN')
print a._Balance
print "\n"

a = c.getOrderHistory('BTC-SRN')
print a._Quantity
print "\n"
