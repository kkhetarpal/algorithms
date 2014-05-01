def ascendsort(X):
    m = len(X)
    for i in range(0,(m-1)):
        for j in range((i+1),m):
            if (X[i] > X[j]):
                X[i] = X[i] + X[j]
                X[j] = X[i] - X[j]
                X[i] = X[i] - X[j]
                j = j+1
        i = i+1
    return X
   

A = []
B = []
#Y = [5,4,1,8,7,2,6,3]
Y = [9,1,5,3,8,2,11,7]
n = len(Y)
for k in range(0,n/2):
    A.append(Y[k])
for k in range(n/2,n):
    B.append(Y[k])
print A
print B

Asorted = ascendsort(A)
Bsorted = ascendsort(B)

print Asorted
print Bsorted
