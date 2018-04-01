# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 08:19:11 2018

@author: bgossage
"""

import numpy
import matplotlib
import matplotlib.pyplot

ngroups = 2
nsamples = 64

k1 = 2.0  # fertilizer gain
k2 = 1.0  # moisture gain
moisture = 20.0


def production( x, w ):

    return  k1 * x + k2 + w

#end function production ~~~~~~~~~~~~~~

def linear_fit ( X, Y, label=str() ):

    Ymean = numpy.mean( Y )

# Construct the measurement matrix and add on a column of ones for the bias term...
    A = numpy.vstack([X, numpy.ones(len(X))]).transpose()

# Compute the least squares solution...
    solution = numpy.linalg.lstsq( A, Y, rcond=-1 )

# Compute and print the sums of squares...

# The fit coefficients are in the first element of the solution (tuple)
    coeffs = solution[0]

    Ypred = A @ coeffs   # NOTE:  '@' is the matrix multiplication operator
    residuals = Y - Ypred
    deviations = Y - Ymean

    RSS = residuals @ residuals.transpose()
    TSS = deviations @ deviations.transpose()

    R2 = 1.0 - RSS /TSS

    print( label, " RSS = ", RSS  )
    print( label, " TSS = ", TSS )
    print( label, " R^2 = ", R2 )

    return coeffs, RSS, TSS

#end function linear_fit() ~~~~~~~~~~~~~~~~~~~~~

###  main program ###########

# Generate a range of fertilizer treatments...
n = 20
half = int(n/2)
X = numpy.linspace( start=0.0, stop=10.0, num=n )

print( "n = ", n )

block1 = range(half,n)
block2 = range(0,half)

# Define indicator matrix...
I = numpy.zeros(n)
I[block1] = 0.0
I[block2] = 1.0

# Divide the treatments areas into dry and moist subgroups...
W = numpy.zeros(n)
W  = moisture * I

Y = numpy.zeros(n)

Y = production( X, W )


# linear fit over all data...
solution = linear_fit( X, Y, "grand" )
m,c = solution[0]

# linear fit over sub-groups...
X1 = X[block1]
Y1 = Y[block1]
solution = linear_fit( X1, Y1, "block1" )
m1,c1 = solution[0]

X2 = X[block2]
Y2 = Y[block2]
solution = linear_fit( X2, Y2, "block2" )
m2,c2 = solution[0]

matplotlib.pyplot.scatter( X, Y )

matplotlib.pyplot.plot(X, m*X + c, 'r', label='global fit')

matplotlib.pyplot.plot(X1, m1*X1 + c1, 'g', label='dry fit')

matplotlib.pyplot.plot(X2, m2*X2 + c2, 'b', label='moist fit')

matplotlib.pyplot.xlabel( "x" )
matplotlib.pyplot.ylabel( "y" )
matplotlib.pyplot.legend(loc='upper right')
matplotlib.pyplot.show()
