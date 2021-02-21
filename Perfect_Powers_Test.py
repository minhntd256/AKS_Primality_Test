import math
from decimal import *


# for i in range(30):
#     print(i,perfectPower(i))



# def perfect_power(n):
#     r = int(math.log(n,2)) + 1
#     l = 2
#     while(True):
#         if(l>r):
#             return False
#         m = (r+l)//2  #chia nguyen
#         k = Decimal.__pow__(Decimal(n),Decimal(1/m))
#         ng = int(k)
        
#         if(k == ng ):
#             return True
#         if(k < ng):
#             l = m + 1
#         else:
#             r = m - 1  
#     return True

#print(perfect_power(443060353998445655840854662515542076714707))
# complexity O(log2(n)) with n is bit number


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