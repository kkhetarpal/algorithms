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
    print a
    print b
    print c
    print d
   

    karatsuba(a,c)
    karatsuba(b,d)
    e = a+b
    f = c+d
    karatsuba(e,f)
    return (a*c*pow(divider,2) + b*d + ((e*f-b*d-a*c)*divider))

x = int(raw_input("Enter first number"))
y = int(raw_input("Enter second number"))
result = karatsuba(x,y)
print result
