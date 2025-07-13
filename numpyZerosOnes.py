import numpy


shape = tuple(map(int,input().split()))
print(shape)
print(numpy.zeros(shape, dtype=numpy.int_))
print(numpy.ones(shape, dtype=numpy.int_))

"""
[[[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]
 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
  
[[[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]
 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
"""