import numpy
n, m = map(int, input().split())
print(n,m)
print([input().split() for i in range(n)])
M = numpy.array([input().split() for j in range(n)], int)
print(M)
print(M.transpose())
print(M.flatten())


