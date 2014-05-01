def swap(array,index1,index2):
    temp = array[index1] 
    array[index1] = array[index2]
    array[index2] = temp
    return;

def recsort(X,startpoint):
    m = len(X)
    if (startpoint == (m-1)):
        return;
    else:
        minindex = startpoint
        for i in range(startpoint,m):   
            if(X[i] < X[minindex]):
                minindex = i
        swap(X,startpoint,minindex)
        recsort(X,(startpoint+1))
    return;
   

A = []
B = []
#Y = [5,4,1,8,7,2,6,3]
Y = [1,3,-4,-9,2,-1,8,6]
n = len(Y)
for k in range(0,n/2):
    A.append(Y[k])
for k in range(n/2,n):
    B.append(Y[k])
#print A
#print B

#recursively sort any array X
recsort(A,0)
recsort(B,0)
#print A
#print B

#perform a merge of the two half arrays
C = []
i = 0
j = 0
for k in range(0,n):
    while i<n/2 and j<n/2:
        if (A[i] < B[j]):
            C.append(A[i])
            #print C
            i=i+1
        elif (B[j] < A[i]):
            C.append(B[j])
            #print C
            j=j+1
    while i<n/2:
        C.append(A[i])
        i = i+1
    while j<n/2:
        C.append(B[j])
        j = j+1
    k = k+1
print C





