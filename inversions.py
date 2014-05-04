#Counting Inversions : Brute force algorithm

# A brute force algorithm would be to compare each element in both arrays to each other, and determine if they would need to be swapped. 

#This is O(n^2) (quadratic in n). 

def inversion_count(arr,n):
    invcount = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (arr[i]>arr[j]):
                invcount = invcount+1
    return invcount

arr=[1,3,5,2,4,6]
n= len(arr)
count = inversion_count(arr,6)
print "The number of inversions are ",count
# print count
