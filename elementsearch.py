#search for an element in an array 


def search(element,array):
    n = len(array)
    for i in range(0,n):
        if (X[i] == element):
            return 1
    return 0



X = [8,7,6,5,77,10,1,36,4,0,11,15,3]
number = int(raw_input("Enter the element you want to search"))
t = search(number,X)
if t == 1:
    print "Found a Match"



#The Running time for this example is O(n) in terms of the Big O notation. 
