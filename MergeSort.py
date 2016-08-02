# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:43:01 2016

@author: ForestWang
"""

# Inversion counts

def merge(A, B):
    lenA = len(A); lenB = len(B)
    C = []; i=0; j =0
    while(i<lenA and j<lenB):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if lenA-i != 0:
        for k in range(lenA -i):
            C.append(A[i+k])
    if lenB-j != 0:
        for k in range(lenB -j):
            C.append(B[j+k])
    return C

def sort(X):
    lenX = len(X)
    if lenX == 1:
        return X
    A = X[:(lenX/2)]; B = X[(lenX/2):]
    A = sort(A)
    B = sort(B)
    R = merge(A, B)
    return R

if __name__ == "__main__":
    X = [5,1,4,3,6,2]
    R = sort(X)
    print R