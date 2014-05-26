#The file contains all of the integers between 1 and 10,000 (inclusive) 
#in unsorted order (with no integer repeated). 
#The integer in the ith row of the file gives you the ith entry of an input array.
#Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. 
#As you know, the number of comparisons depends on which elements are chosen as pivots, 
#so we'll ask you to explore three different pivoting rules.
#You should not count comparisons one-by-one.
#For the first part of the programming assignment, 
#you should always use the first element of the array as the pivot element. 

def quicksort(A,begin,end) :
	count = 0
	if end - begin <= 1:
		return 0
	else :
		split = partition(A,begin,end)
		count = end - begin - 1
		lc = quicksort(A,begin,split)				
		rc = quicksort(A,split+1,end)
		return count + lc + rc


def partition(A,begin,end) :
	pivot = A[begin]
	i = begin + 1

	for j in range(begin+1,end) :
		if A[j] < pivot :					
			A[i], A[j] = A[j], A[i]
			i = i + 1			

	A[i-1], A[begin] = A[begin], A[i-1]
	return i-1



filename = 'argv.txt'   #input file from coursera 
f = open(filename)
data = f.readlines()
f.close()


for i in range(0,len(data)):
    data[i] = int(data[i])



print len(data)
print quicksort(data,0,len(data))

