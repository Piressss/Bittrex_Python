#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

sys.path.append('../src/')

from ApiAccessClass import *

c = ApiAccessClass()

print 'Market Request'
print c.getAPI('getopenorders', 'BTC-XRP')
print '\n'

print 'Public Request'
print c.getAPI('getticker', 'BTC-XRP')
print '\n'

print 'Account Request'
print c.getAPI('getbalance', 'BTC-SRN')
print '\n'

print 'Public V2 Candles'
print c.getAPI('GetTicks', 'BTC-XVG')
print '\n'
