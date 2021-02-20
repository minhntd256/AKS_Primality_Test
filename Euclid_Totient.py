# Python3 program to calculate
# Euler's Totient Function
def phi(n):

    # Initialize result as n
    result = n

    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2
    while(p * p <= n):

        # Check if p is a
        # prime factor.
        if (n % p == 0):

            # If yes, then
            # update n and result
            while (n % p == 0):
                n = int(n / p)
            result -= int(result / p)
        p += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if (n > 1):
        result -= int(result / n)
    return result

#O(φ(n)) = O~(r^0.5)
#  
# Driver Code
# for n in range(1, 11):
#     print("phi(",n,") =", phi(n));

# This code is contributed
# by mits

#O∼(r*sqrt(φ(r)) * log^3(n)) = O∼(r^3/2 * log^3(n)) = O∼(log21/2 n) = O∼(||n||10.5).
