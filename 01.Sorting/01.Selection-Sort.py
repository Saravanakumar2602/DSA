arr = [1,42,4,3,5,3,2,45,9,5]

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j] :
                min = j

        if i != min :
            arr[i],arr[min] = arr[min],arr[i]


selectionSort(arr)
print(arr)
