def truncated_fast_powering(g,a, N):
    u = a
    s = g % N
    c = 1
    while u >= 1:
        if u % 2 != 0:
            c = (c*s)
            if(c > N):
                c = N + 1
                break
        s = (s*s) % N
        u = u//2
    return c

def perfect_power(n):
    b = 2
    if n < 2:
        return True
    while 2**b <= n:
        a = 1
        c = n
        while c - a >= 2:
            m = (a+c)//2
            p = truncated_fast_powering(m,b,n)
            if p == n:
                return True
            if p < n:
                a = m
            else:
                c = m
        b = b + 1
    return False

# for i in range(30):
#     print(i,perfectPower(i))

# complexity O(n^3) with n is bit number