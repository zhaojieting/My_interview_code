"""
this is a quik_sort function for my personal practice
"""
import time


def quik_sort(arr, i, j):
    pivot = arr[i]
    left = i
    right = j
    while i < j:
        while arr[i] < pivot and i < j:
            i += 1
        while arr[j] > pivot and i < j:
            j -= 1
        if j > i:
            arr[j], arr[i] = arr[i], arr[j]
    arr[i] = pivot
    if i - 1 > left:
        quik_sort(arr, left, i-1)
    if i + 1 < right:
        quik_sort(arr, i+1, right)


def pop_sort(arr):
    for k in range(len(arr)):
        for i in range(len(arr))[:-1]:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

a = list(range(100)[::-1])
s = time.time()
for i in range(1000):
    quik_sort(a, 0, 99)
e = time.time()
print((e - s)*1000000)
print(a)
a = list(range(100)[::-1])
s = time.time()
for i in range(1000):
    pop_sort(a)
e = time.time()
print((e - s)*1000000)
print(a)