import math
def fast_powering(g,a, N):
    u = a
    s = g % N
    c = 1
    while u >= 1:
        if u % 2 != 0:
            c = (c*s) % N
        s = (s*s) % N
        u = u//2
    return c


# print(fast_powering(6,1,8))