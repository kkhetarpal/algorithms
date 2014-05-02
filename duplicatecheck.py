array = [1,2,3,4,5,6,7,8,9,10,1]

common = 0
n = len(array)
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i] == array[j]):
            common = common +1
        
if (common >=1):
    print "Found duplicate elements"
else:
    print "no duplicate elements"
            




#The Running time for this example is O(n^2) in terms of the Big O notation. 


#number of operations : n(n-1)/2 which is again quadratic dependence 
