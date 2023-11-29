heap = [] #maxHeap
while True:
    if(input("Do you want to add value: ") == "1"):
        value = int(input("Enter Value: "))
        heap.append(value)
        i = len(heap) - 1
        while heap[i] > heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i //= 2
    else:
        break
    
print(heap)