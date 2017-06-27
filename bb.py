#!/bin/python3

import sys
def bubble_sort(a):
    n = len(a)
    ct = 0
    for i in range(n):
        sw = 0
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                sw+=1
                ct+=1
                a[j],a[j+1] = a[j+1],a[j]
        if sw==0:
            break
    return ct,a
            
n = int(input().strip())
a = list(map(int,input().strip().split(' ')))
count, sa = bubble_sort(a)
    
        
print('Array is sorted in' ,count, 'swaps.')
print('Sorted array is')
for x in sa:
    print(x ,end = ' ')