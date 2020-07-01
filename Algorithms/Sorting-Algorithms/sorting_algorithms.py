# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lst = [9,8,7,6,5,4,3,2,1]
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        j = i
        while j>0 and lst[j-1]>current:
             lst[j] = lst[j-1]
             j-=1
        lst[j]=current
    return lst
print(insertion_sort(lst))