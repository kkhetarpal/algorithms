









def partition(A,l,r):
    pivot = A[l]
    i = l + 1
    
    for j in range(l+1,r):
        if A[j] < pivot :
            A[j], 
            i = i + 1
    
    A[i-1], A[l] = A[l], A[i-1]
    return i-1
