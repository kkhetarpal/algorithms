#search for an element in two arrays 


def twoarraysearch(element,array1,array2):
    n1 = len(array1)
    n2 = len(array2)
    for i in range(0,n1):
        if (array1[i] == element):
            return 1
    for j in range(0,n2):
        if (array2[j] == element):
            return 1
    return 0



X = [8,7,6,5,77,10,1,36,4,0,11,15,3]
Y = [99,11,22,33,44,55,66,77,88,100]
number = int(raw_input("Enter the element you want to search"))
t = twoarraysearch(number,X,Y)
if t == 1:
    print "Found a Match"
else:
    print "No Match Found"



#The Running time for this example is O(n) in terms of the Big O notation. 

#Number of operations is roughly 2n

#However 2 being a constant is supressed when we pass it to the Big O notation
