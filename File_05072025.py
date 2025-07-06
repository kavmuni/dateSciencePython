import platform
import sys
import json

print("Hello world")

x = 10
print(type(x))
x = 'String'
print(type(x))
x = '10'
print(type(x))
print(platform.architecture()) # ('64bit', 'WindowsPE')

print("int(0) is of ", sys.getsizeof(0),"bytes")
print("float(1.315478) is of ", sys.getsizeof(1.315478),"bytes")
print("complex(13+13j) is of ", sys.getsizeof(13+13j), "bytes")

#help("string")
# list
fruitList = ['mango', 'banana', 'jackfruit', 'guava']
for e in fruitList:
    print(e)

print(sys.getsizeof(fruitList))

emptyList=[]
print(sys.getsizeof(emptyList))

# tuple
tuple1 = ()
print(sys.getsizeof(tuple1))
tuple2 = (1,2,3,4,5,4,3,2,'test')
for e in tuple2:
    print(type(e))
print(sys.getsizeof(tuple2))

#set
set1 = {}
set2 = {'abc', 1,2,4}
print(set2)
set2.remove(2)
print(set2)
set2.add('Muni')
print(set2)

# dict
dict1 = {1:'abc', 2:'def', 4:'ijk', 3:'lmn', 'cd':3, (1,2,3): 345}
print(dict1)
print(dict1.keys())
print(dict1.values())
print(type(dict1.values()))

# duplicae keys are allowed and the latest key will replace the old value
dict2={"name":'name1', "name":"name2"}
print(dict2) # {'name': 'name2'}