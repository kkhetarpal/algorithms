

def closestpair(arr,n):
    dmin = 10000000
    imin = 0
    jmin = 0
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            d = (arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2
            #print d
            if d < dmin:
                dmin = d
                imin = i
                jmin = j
    return imin,jmin


P = [[1,2],[3,4],[7,8],[0,7],[0,4],[4,7]]
length = len(P)
#print length
pairs = closestpair(P,length)
#print P[closestpair(P,length)]
print P[pairs[0]],P[pairs[1]]
