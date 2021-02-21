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

    #tests(200000,300000)

    #n = 714051848632075255270846065582254824974731954656694495015002723456344967852398518444344494100019940697941809328793646137540264966485491570297895858497510984056184588984077016442000974612321787833605579742970659655607993091
    n = 309378619739821072136675084704881432385295816977478367188677

    print(f'- n: {n}\n- bit length: {n.bit_length()}')
    ret = AKS_Wrapper(n)
    cProfile.run(f'AKS_Wrapper({n})')
    print(ret)
