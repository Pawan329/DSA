'''
The selection sort algorithm sorts an array by repeatedly finding the minimum 
element (considering ascending order) from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array. 

1) The subarray which is already sorted. 

2) Remaining subarray which is unsorted. In every iteration of selection sort, 
the minimum element (considering ascending order) from the unsorted subarray is picked 
and moved to the sorted subarray. 
'''


data = [5, 4, 3, 2, 1]

for j in range(len(data)-1):
    for i in range(j, len(data)-1):
        if data[i] > data[i+1]:
            min_index = i+1

    temp = data[j]
    data[j] = data[min_index]
    data[min_index] = temp
    
print(data)