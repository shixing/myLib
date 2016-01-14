import random

def get_different_random_numbers(n,m):
    '''
    n = [0,1,...,n-1]
    return m different random numbers from n
    '''
    l = range(n)
    for end in xrange(n - 1, n-m-1, -1):
        r = random.randint(0, end)
        tmp = l[end]
        l[end] = l[r]
        l[r] = tmp
    return l[n-m:]

