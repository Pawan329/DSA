'''
The selection sort algorithm sorts an array by repeatedly finding the minimum 
element (considering ascending order) from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array. 

1) The subarray which is already sorted. 

2) Remaining subarray which is unsorted. In every iteration of selection sort, 
the minimum element (considering ascending order) from the unsorted subarray is picked 
and moved to the sorted subarray. 
'''

data = [10, 6, 12, 14, 2, 21, 25]

for i in range(len(data)-1):
    
    min_index = i
    
    for j in range(i+1, len(data)-2):
        if data[j] < data[i]:
            min_index = j
    
    temp = data[i]
    data[i] = data[min_index]
    data[min_index] = temp
    
print(data)