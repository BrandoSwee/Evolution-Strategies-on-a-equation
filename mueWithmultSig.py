# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:32:38 2022

Brandon Sweeney
bpsweeney@alaska.edu

"""

import numpy as np
import math

def Mutation(individual):
    n = len(individual[0])
    sigmaPrimes = []
    newVals = []
    i = 0
    TooManyAttempts = 0
    while(len(sigmaPrimes) != n):
        normDistVals = np.random.normal(0.0, 1.0, 2)
        #for j in range(len(normDistVals)):
            #print(normDistVals[j])
        sigmaPri = ( individual[1][i] * math.exp( ((1.0/(math.sqrt(2.0 * n))) * normDistVals[0]) + ( (1.0/(math.sqrt(2.0 * math.sqrt(n)))) * normDistVals[1]) ))
        if(sigmaPri > 0.0 and sigmaPri < 10.0):
            sigmaPrimes.append(sigmaPri)
            i = i + 1
            TooManyAttempts = 0
        else:
            TooManyAttempts = TooManyAttempts + 1
        # Really don't want to set it.
        if(TooManyAttempts == 100):
            if(sigmaPri <= 0.0):
                sigmaPri = 0.01
                sigmaPrimes.append(sigmaPri)
                i = i + 1
                TooManyAttempts = 0
            else:
                sigmaPri = 9.99
                sigmaPrimes.append(sigmaPri)
                i = i + 1
                TooManyAttempts = 0
        
    i = 0
    ## upperbound of 10 on sigmaPrime
    ## stops infinte loops for now
    TooManyAttempts = 0
    while(len(newVals) != n):
        normDistVals = np.random.normal(0.0, 1.0, 1)
        newpoint = individual[0][i] + sigmaPrimes[i] * normDistVals[0]
        if(i == 0 and newpoint <= 12.0 and newpoint >= -3.0):
            newVals.append(newpoint)
            i = i + 1
            TooManyAttempts = 0
            
        elif(i == 1 and newpoint <= 6.0 and newpoint >= 4.0):
            newVals.append(newpoint)
            i = i + 1
            TooManyAttempts = 0
            
        else:
            TooManyAttempts = TooManyAttempts + 1
            
        if(TooManyAttempts == 11):
            if(i == 0):
                if(newpoint > 12.0):
                    newpoint = 12.0
                    newVals.append(newpoint)
                else:
                    newpoint = -3.0
                    newVals.append(newpoint)
                i = i + 1
                TooManyAttempts = 0
                
            elif(i == 1):
                if(newpoint > 6.0):
                    newpoint = 6.0
                    newVals.append(newpoint)
                else:
                    newpoint = 4.0
                    newVals.append(newpoint)
                i = i + 1
                TooManyAttempts = 0
            ##Error of some sort
            else:
                break
    
    retur = [newVals,sigmaPrimes]
    return retur
    
if __name__ == "__main__":
    indi = [[6.0, 5.0],[1.0,1.0]]
    out = Mutation(indi)
    print(out)
