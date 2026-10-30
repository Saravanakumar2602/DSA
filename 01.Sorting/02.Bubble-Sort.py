arr = [1,42,4,3,5,3,2,45,9,5]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(1,n-i):
            if arr[j-1] > arr[j] :
                arr[j-1],arr[j] = arr[j],arr[j-1]
            


bubbleSort(arr)
print(arr)
