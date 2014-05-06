#iterative matrix multiplication

a = [[1,2,3],[1,2,3],[1,2,3]]
b = [[1,2,3],[1,2,3],[1,2,3]]
# print a[0]
# print a[1]
n = 3
c = [] # just a list ... NOT a list of lists
for i in xrange(n):
    c.append([]) # append another empty list ... this makes space for elements
    for j in xrange(n):
        sum = 0
        for k in xrange(n):
            sum += a[i][k]*b[k][j]
        c[i].append(sum)
print c
