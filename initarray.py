#initialize n dimension array in python

#method1
##intialize to 0
nrows = 3
ncolumns = 4
arr1 = [[0 for i in xrange(ncolumns)] for j in xrange(nrows)]
print arr1



#method2

import random
arr2 = [[random.random() for i in xrange(ncolumns)] for j in xrange(nrows)]
print arr2


