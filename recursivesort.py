# def swap(array,index1,index2):
#     array[index1] = array[index1] + array[index2]
#     array[index2] = array[index1] - array[index2]
#     array[index1] = array[index1] - array[index2]
#     return;


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
        for i in range(startpoint,m):    #find smallest element index
            if(X[i] < X[minindex]):
                minindex = i
        #if(startpoint!=minindex):       #no need to swap if startpoint holds min element
        swap(X,startpoint,minindex)
        recsort(X,(startpoint+1))
    return;
   

A = []
B = []
Y = [5,4,1,8,7,2,6,3]
#Y = [1,2,3,4,7,8,6,9]
n = len(Y)
for k in range(0,n/2):
    A.append(Y[k])
for k in range(n/2,n):
    B.append(Y[k])
print A
print B

#recursively sort any array X
recsort(A,0)
recsort(B,0)
print A
print B







