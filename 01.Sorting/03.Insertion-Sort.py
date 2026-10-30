arr = [1,42,4,3,5,3,2,45,9,5]

def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j > 0 and arr[j-1]>arr[j] :
            arr[j-1] ,arr[j] = arr[j],arr[j-1]
            j-=1
            
            


insertionSort(arr)
print(arr)
