#!/bin/python3

import sys


def merge_sort(A):
    if len(A) <= 1:
        return 0, A
    middle = int(len(A)/2)
    left_inversions, left = merge_sort(A[:middle])
    right_inversions, right = merge_sort(A[middle:])
    merge_inversions, merged = merge(left, right)
    inversions = left_inversions + right_inversions + merge_inversions
    return inversions, merged
def merge(left, right):
    result = []
    i, j, inversions = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            inversions += j
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    inversions += j*(len(left)-i)
    result += left[i:]
    result += right[j:]
    return inversions, result


n = int(input().strip())
a = list(map(int,input().strip().split(' ')))
count, sa = merge_sort(a)
    
        
print('Array is sorted in' ,count, 'swaps.\nFirst Element:',sa[0], '\nLast Element:',sa[n-1])
