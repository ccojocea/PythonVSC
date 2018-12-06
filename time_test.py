import time as t 
import timeit


def f1(n): 
    return ''.join([str(x) for x in range(n)]) 
    
def f2(n): 
    s = '' 
    for x in range(n): 
        s += str(x) 
    return s 
    
n = 10**6 

#t1 = t.time() 
#f1(n) 
#t2 = t.time() 
#f2(n) 
#t3 = t.time() 

#print(t2 - t1)
#print(t3 - t2)

#print(t3 - t2 > t2 - t1)

#m = f2(n)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(f2, n)

print(timeit.timeit(wrapped, number=1))

#print(timeit.timeit(m, number = 1))

#print(timeit.timeit('s = ""\nfor x in range(1000000):\n\ts += str(x)', number = 1))