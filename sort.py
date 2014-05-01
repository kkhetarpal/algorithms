#A = [5,4,1,8]
A = [7,2,3,6]
#A = [9,1,8,10]
#simple asceding order sort


n = len(A)
for i in range(0,(n-1)):
    for j in range((i+1),n):
        if (A[i] > A[j]):
            A[i] = A[i] + A[j]
            A[j] = A[i] - A[j]
            A[i] = A[i] - A[j]
        j = j+1
    i = i+1

print A

