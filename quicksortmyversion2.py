#l : leftmost begin of the array
#r : rightmost end of the array
#A : array 
#split : hold the position of the partition starting
#count : holds the number of comparisons for each sub recursive call
#to keep count adding (length - 1) to the running total of the comparisons, since pivot element is compared to each (length - 1) elements.  


def quicksort(A,l,r):
    if r-l <= 1 :                          #base case of only 1 element
        return 0
    else:
        A[l], A[r-1] = A[r-1] , A[l]       #swap the first with last element which is pivot, this now becomes the same as pivot with first element. 
        split = partition(A,l,r)           #partitions the array around pivot
        count = r - l - 1                  #number of comparisons made
        lc = quicksort(A,l,split)          #left comparisons after partition
        rc = quicksort(A,split+1,r)        #right comparisons after partition
        return lc + rc + count


def partition(A,l,r):
    pivot = A[l]                           #last element as pivot
    i = l + 1                              #partitioning needed from first but 1
    
    for j in range(l+1,r):                 #scan through the elements
        if A[j] < pivot :                  #if element < pivot 
            A[i],A[j] = A[j],A[i]          #swap 
            i = i + 1
    
    A[i-1], A[l] = A[l], A[i-1]            #after paritioned, place the pivot in the right place
    return i-1                             #hold the position of the start of partition


filename = 'quicksort.txt'
f = open(filename)
data = f.readlines()
f.close()

for i in range(0,len(data)):
    data[i] = int(data[i])

print len(data)
print quicksort(data,0,len(data))          #gives the number of comparisons 
