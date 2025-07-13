import numpy

# array_1 = numpy.array([[1,2,3], [3,2,1]]) # matrix
# array_2 = numpy.array([[9,8,7], [7,8,9]])
# array_3 = numpy.concatenate((array_1, array_2), axis=1)
# print(array_3)

n,m,p = map(int, input().split())
array_1 = numpy.array([input().split() for i in range(n)], int)
array_2 = numpy.array([input().split() for j in range(m)], int)
print(numpy.concatenate((array_1, array_2), axis=0))

