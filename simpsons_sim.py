# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:19:11 2018

@author: bgossage
"""

import numpy

ngroups = 2
nsamples = 64
k0 = 1.0  # offset
k1 = 1.0  # fertilizer gain
k2 = 19.0  # moisture gain
moist = 29.0
dry = 0.0;

def production( x, w ):

    return  k0 + k1 * x + k2 + w

#end function production


print( "Production = ",  production(1.0,0.0) )

# Generate a range of fertilizer treatments...
n = 20
half = int(n/2)
X = numpy.linspace( start = 0.0, stop=10.0, num=n )

print( "n = ", n )

# Divide the treatments areas...
# two subgroups...
W = numpy.zeros(n)
W[half:n] = moist
W[0:half-1] = dry

Y = numpy.zeros(n)

for i in range(0,n):
    Y[i] = production( X[i], Y[i] )

print( "Y=", Y )


