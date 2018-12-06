import timeit

#'0-1-2-3-.....-99'

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit.timeit('x = "-".join(map(str,range(100)))', number=10000))

print('"-".join(map(str,range(100)))')