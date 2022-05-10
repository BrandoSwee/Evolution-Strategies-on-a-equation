# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:53:31 2022

Brandon Sweeney
bpsweeney@alaska.edu

Jacob Keeler
jckeeler@alaska.edu

Paul James Natcher
pjnatcher@alaska.edu

"""

import numpy as np
import random
import copy
import math
import matplotlib.pyplot as plt
from mueWithmultSig import Mutation
from recombination import recomb

def findVal(indi):
    num = 21.5 + (indi[0][0] * math.sin(4.0 * math.pi * indi[0][0])) + (indi[0][1] * math.sin(20.0 * math.pi * indi[0][1]))    
    return num

def runEval(offspring, currPop, population):
    #1st recombinate 
    offSpring = []
    for n in range(offspring):
        parent1 = random.randint(0, (population - 1))
        parent2 = random.randint(0, (population - 1))
        while(parent1 == parent2):
            parent2 = random.randint(0, (population - 1))
        z = recomb(currPop[parent1],currPop[parent2])
        offSpring.append(copy.deepcopy(z))
    mueOff = []
    #2nd mutate all offspring
    for n in range(offspring):
        mueOff.append(Mutation(offSpring[n]))
    values = []
    offSpring = mueOff
    for i in range(len(offSpring)):
        value = findVal(offSpring[i])
        values.append([value, i])
    values.sort()
    values.reverse()
    outVals = []
    outPop = []
    for i in range(population):
        outVals.append([values[i][0],i])
        outPop.append(copy.deepcopy(offSpring[values[i][1]]))
    
    return outPop, outVals

def main():
    ## Make sure your popluation is not smaller than offspring. This will cause
    ##                                                          an error.
    population = 50
    offspring = 350
    intialSig = 1.0
    fitnessEvals = 750 # technically population evals. Actual
                        # fitness evals = offspring * fitnessEvals
    ############# 
    # seed settings
    seed = 43310
    #seed = 9893402
    #seed = 41
    random.seed(seed)
    np.random.seed(seed)
    #############
    # In this case an individual looks like:
    # [[x1,x2],[sig1,sig2]]*
    sizeOfindividual = 2  # This is the n value unused
    x1plot = []
    x2plot = []
    yplot = []
    numplot = []
    currPop = []
    Vals = []
    colorsForScatt= []
    for i in range(population):
        ## problem specific
        x1 = random.uniform(-3.0, 12.0)
        x2 = random.uniform(4.0,6.0)
        currPop.append([[x1,x2],[intialSig,intialSig]])
        
    for i in range(len(currPop)):
        value = findVal(currPop[i])
        ########### value and index of individual in popu
        Vals.append([value, i])
    #for i in range(len(currPop)):
    #    print(currPop[i])
    #    print(Vals[i])
    #This is population 0
    # x1, x2, and y plots will be averages
    # num will be number for population y
    numplot.append(0)
    total = 0
    totx1 = 0
    totx2 = 0
    for i in range(population):
        total = total + Vals[i][0]
        totx1 = totx1 + currPop[i][0][0]
        totx2 = totx2 + currPop[i][0][1]
    average = total / population
    averagex1 = totx1 / population
    averagex2 = totx2 / population
    yplot.append(average)
    bestyave = average
    bestx1ave = averagex1
    bestx2ave = averagex2
    bestIndi = [0,[0,0]]
    populationBestIndiWasFirstFoundIn = 0
    populationNumber = 0
    x1plot.append(averagex1)
    x2plot.append(averagex2)
    colorsForScatt.append("blue")
    ## Start program
    for v in range(fitnessEvals):
        #currPop, Vals = runEval(offspring,currPop,population)
        currPop, Vals = runEval(offspring,currPop,population)
        numplot.append(v + 1)
        total = 0
        totx1 = 0
        totx2 = 0
        if(bestIndi[0] < Vals[0][0]):
            bestIndi[0] = Vals[0][0]
            bestIndi[1][0] = currPop[0][0][0]
            bestIndi[1][1] = currPop[0][0][1]
            populationBestIndiWasFirstFoundIn = v + 1
        for i in range(population):
            total = total + Vals[i][0]
            totx1 = totx1 + currPop[i][0][0]
            totx2 = totx2 + currPop[i][0][1]
        #print(bestIndi)
        average = total / population
        averagex1 = totx1 / population
        averagex2 = totx2 / population
        if(average > bestyave):
            bestyave = average
            bestx1ave = averagex1
            bestx2ave = averagex2
            populationNumber = v + 1
        yplot.append(average)
        x1plot.append(averagex1)
        x2plot.append(averagex2)
        colorsForScatt.append("blue")
    
    colorsForScatt[populationNumber] = "red"
    
    plt.scatter(x1plot,x2plot, color=colorsForScatt)
    plt.show()
    plt.clf()
    plt.plot(numplot, yplot)
    plt.show()
    plt.clf()
    print("The best population was population", populationNumber)
    print("with an average value in the population being", bestyave)
    print("Average x1 and x2 values for population", populationNumber,"were")
    print("x1:",bestx1ave, "and")
    print("x2:",bestx2ave, "\n")
    print("Value of the best individual found was",bestIndi[0])
    print("It first appeared in population:", populationBestIndiWasFirstFoundIn)
    print("With a x1 and x2 of\nx1:", bestIndi[1][0], "and")
    print("x2:", bestIndi[1][1])
    #print(currPop)
    #print(Vals)
    
    
    
    
if __name__ == "__main__":
    main()