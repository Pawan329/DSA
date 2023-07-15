# Bubble sorting
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 

temp = [5,6,3,20,1]

for i in range(0,len(temp)-1):
    for i in range(0, len(temp)-1):
        if temp[i+1] < temp[i]:
            large_val = temp[i]
            smaller_val = temp[i+1]
            temp[i] = smaller_val
            temp[i+1] = large_val
        
print(temp)
