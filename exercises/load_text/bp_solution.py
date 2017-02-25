import numpy as np

arr1 = np.loadtxt('float_data.txt',dtype='int32')

arr2 = np.loadtxt('float_data_with_header.txt',skiprows=1)

print(arr2)

arr3 = np.loadtxt('complex_data_file.txt',skiprows=1,comments='%',
                  usecols=(0,1,2,4),dtype='int32',delimiter=','
                  )
print(arr3)