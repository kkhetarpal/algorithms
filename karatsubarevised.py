def karatsuba(x,y):
    if x < 10 and y <10:
        return x*y
    else:
        if x > y:
            divider = pow(10,len(str(x))/2)
        else:
            divider = pow(10,len(str(y))/2)
    a = x // divider
    b = x % divider
    c = y // divider
    d = y % divider
 

    l = karatsuba(a,c)
    m = karatsuba(b,d)
    e = a+b
    f = c+d
    n = karatsuba(e,f)
    return (l*pow(divider,2) + m + ((n-m-l)*divider))

x = int(raw_input("Enter first number"))
y = int(raw_input("Enter second number"))
result = karatsuba(x,y)
print result
