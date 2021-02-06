def perfect_power(n):
    b = 2
    if n < 2:
        return True
    while 2**b <= n:
        a = 1
        c = n
        while c - a >= 2:
            m = (a+c)//2
            p = min(m**b, n+1)
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