array1 = [1,2,3,4,5,6,7,8,9,10]
array2 = [1,3,5,11,12,13,14,15,27,88]

common = 0
n = len(array1)
for i in range(0,n):
    for j in range(0,n):
        if (array1[i] == array2[j]):
            common = common +1
        
if (common >=1):
    print "Found ",common, "common elements"
            




#The Running time for this example is O(n^2) in terms of the Big O notation. 
