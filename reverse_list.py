# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/22/2023
# Description: Function that takes a list and reverses the order of the elements in the list
#              without using slices.

def reverse_list(vals):
    """Returns the values of the list in reverse order"""
    i = 0
    j = len(vals)-1 # index length of list minus 1
    while(i<j):
        num = vals[i]
        vals[i] = vals[j]
        vals[j] = num
        i+=1
        j-=1

# vals = [7, -3, 12, 9]
# reverse_list(vals)
# print(vals)