# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:30:32 2022

Brandon Sweeney
bpsweeney@alaska.edu

"""
import random

def recomb(parent1, parent2):
    newIndiVals = []
    for i in range(len(parent1[0])):
        num = random.randint(0,1)
        if(num == 0):
            newIndiVals.append(parent1[0][i])
        else:
            newIndiVals.append(parent2[0][i])
    newSigma = []
    for i in range(len(parent1[1])):
        sigma = ((parent1[1][i] + parent2[1][i]) / 2)
        newSigma.append(sigma)
    
    indi = [newIndiVals, newSigma]
    return indi
    
    
if __name__ == "__main__":
    indi = [[6.0, 5.0],[1.3,1.0]]
    bindi = [[4.0, 6.0],[1.0,1.2]]
    out = recomb(indi, bindi)
    print(out)
