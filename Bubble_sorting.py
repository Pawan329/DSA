# Bubble sorting
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 

data = [10, 6, 12, 14, 2, 21, 25]

for i in range(len(data)-1):
    
    for j in range(0, len(data)-1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
        
print(data)


