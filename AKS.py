from Perfect_Powers_Test import perfect_power
from Euclid_GCD import gcd
from Fast_Powering import fast_powering
from Euclid_Totient import phi
from test import test
import time
import math
def AKS(n):
    #step 1
    #checks if n is a power of an integer where the exponent is greater than 1
    if perfect_power(n): return 'COMPOSITE'
    #step 2
    #looks for the smallest value of r such that there is no k satisfying the equation 
    # n^k = 1 (mod r) for some 1 <= k <= log2 n
   
    limit = int(math.floor(math.log(n,2)))
    r = 2
    flag = True
    while flag:
        flag = False
        for k in range(1, limit+ 1):
            if fast_powering(n,k,r) == 1:
                flag = True
                r += 1
                break
    # = log^2(n)log(r) ~=  ~= O(log^7(n))
    # print(r)
    # step 3
    # checks if n shares a common nontrivial factor with any number a <= r
    for a in range(1, r+1):
        _gcd = gcd(n,a)
        if _gcd > 1 and _gcd < n:
            #print(_gcd)
            return 'COMPOSITE'

    # Complexity = O(r. log^2(n)) ~=O(log^5(n). log^2(n)) = O(log^7(n)) ~= O(||n||^7)

    #step 4
    if n <= r:
        return 'PRIME'
    

    #step 5 + 6
    l = int(math.floor(math.sqrt(phi(r))*math.log(n,2)))
    for a in range(0,l+1):
        # print(fast_powering(a,n,n),fast_powering(a,1,n))
        if fast_powering(a,n,n) != fast_powering(a,1,n):
            return 'COMPOSITE'
    #step 7
    return 'PRIME'
li = []

start = time.time()
for i in range(1,10000):
    if AKS(i) == 'PRIME':
        li.append(i)
print(list(set(li[:]) - set(test)))


# print(AKS(1729))


# print(AKS(443060353998445655840854662515542076714707))
# print(AKS(299153601653415748067823416186657916557))
# x = 443060353998445655840854662515542076714707
# x=1234567
# print(AKS(x))
# print(math.log(x))
end = time.time()
print(end-start)
