import time

class RationalError(ValueError):
    pass



def test(n):
    t1 = time.time()
    ls = []
    for i in range (n*10000):
        ls += [i]
    t2 = time.time()
    ls2 = []
    for i in range(n*10000):
        ls2.append(i)
    t3 = time.time()
    ls3 = [i for i in range(n*10000)]
    t4 = time.time()
    ls4 = list(range(n*10000))
    t5 = time.time()
    raise RationalError('fuck')
    return (t2 - t1, t3-t2, t4-t3, t5-t4) + (ls, ls2, ls3, ls4)

if __name__ == '__main__':
    s = test(8)
    print(s)
