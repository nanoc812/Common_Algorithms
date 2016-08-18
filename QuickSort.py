# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:25:06 2016

@author: ForestWang
"""
#   This function takes the first elements, the last elements and the median of 
#   the fisrt, the last and the median element as pivot. 
#   And I prsent 4 different ways to complete QuickSort by using the last elements
#   as the pivot.

def partition_1st(arr, low, high):
    i = low-1
    pivot = arr[low]
    for j in range(low , high+1):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i], arr[low] = arr[low],arr[i]
    return i

def partition_last(arr, low, high):
    # use the last element as the pivot
    arr[high], arr[low] = arr[low],arr[high]
    i = partition_1st(arr, low, high)
    return i

def partition_median(arr, low, high):
    # use the median the three elements (first, last, median of the array) as the pivot
    ip = MedianOfThree(arr, low, high)
    arr[ip], arr[low] = arr[low],arr[ip]
    i = partition_1st(arr, low, high)
    return i

def MedianOfThree(A, l, r):
    if r-l+1 <3:
        return l
    m = int(round((r-l+1)/2.0))-1+l
    if abs(A[l]-A[m]) < abs(A[r]-A[m]) and abs(A[l]-A[r]) < abs(A[r]-A[m]):
        return l
    elif abs(A[r]-A[l]) < abs(A[l]-A[m]) and abs(A[r]-A[m]) < abs(A[l]-A[m]):
        return r
    elif abs(A[m]-A[l]) < abs(A[l]-A[r]) and abs(A[m]-A[r]) < abs(A[r]-A[l]):
        return m

def partition_last_1(arr, low, high):
    i = low-1
    pivot = arr[high]     # pivot
    for j in range(low , high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return i+1

def partition_last_2(arr,low,high):
    i = high-1
    pivot = arr[high]
    j = high-1
    while(j > -1):
        if arr[j] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
        j -= 1
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return i+1

def partition_last_3(arr, low, high):
    i = high; j = 0
    p = arr[high]
    while(j<i):
        if arr[j] > p:
            while(i>j):
                i -= 1
                if arr[i] < p:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


#   Function to do QuickSort
def quickSort(arr,low,high, count):
    if low < high:
        count += high-low
        ## You can rewrite this line below to change the pivot-selection rule
        pi = partition_1st(arr,low,high)
        #pi = partition_median(arr,low,high)
        #pi = partition_last(arr,low,high)
        
        #pi = partition_last_1(arr,low,high)
        #pi = partition_last_2(arr,low,high)
        #pi = partition_last_3(arr,low,high)

        count = quickSort(arr, low, pi-1, count)
        count = quickSort(arr, pi+1, high, count)
    return count

#   The main function that implements QuickSort
#   arr[]: Array to be sorted,
#   low: Starting index,
#   high: Ending index
#   pi: the index of the pivot
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    count = 0
    count = quickSort(arr,0,len(arr)-1, count)
    print 'Number of comparison is: ', count, ', and the sorted array is: ', arr