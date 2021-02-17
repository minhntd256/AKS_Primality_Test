import time
import sympy # baseline
import cProfile

from AKS import AKS

def AKS_Wrapper(n):
    return AKS(n) == 'PRIME'

def tests(lowlim, uplim):
    start = time.time()
    exception = 0
    for n in range(lowlim,uplim):
        if(sympy.isprime(n) != AKS_Wrapper(n)):
            exception = n
            break
    end = time.time()
    print(f'Passed tests from {lowlim}-{uplim}' if exception == 0 else f'Failed at {exception}')
    print(f'Took {end - start}')

if __name__ == '__main__':

    tests(1,10000)

    n = 42575634430603539984456558408546625155420767147071233135436412312415354234123443
    print(f'- n: {n}\n- bit length: {n.bit_length()}')

    cProfile.run(f'AKS_Wrapper({n})')