import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    lArray = arr.reverse()
    print (lArray)
    return numpy.array(lArray, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)