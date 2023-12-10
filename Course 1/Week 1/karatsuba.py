

def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)),len(str(y)))
        n2 = n // 2

        a = x // 10**(n2)
        b = x % 10**(n2)
        c = y // 10**(n2)
        d = y % 10**(n2)
        p = a + b
        q = c + d

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        pq = karatsuba(p,q)
        adbc = pq - ac - bd

        return (ac * 10**(2*n2)) + (adbc * 10**(n2)) + (bd)

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsuba(x,y))

# x*y = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184