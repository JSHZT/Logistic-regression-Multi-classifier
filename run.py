def fun(m, n):
    if m % n is 0:
        return n
    else:
        r = m % n
        m = n
        n = r
        return(fun(m, n))
        

def lcm(x, y):
    a = x * y
    b = fun(x, y)
    print(b)
    c = a / b
    print(c)
    
x, y = map(int, input().split())
lcm(x, y)