#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:28:24 2019

@author: rakeshkatkam
@course: Machine Learning, Summer 2019, Grade: A
@program: M.S, Department of Computer Science and Mathematics
@school: University of Central Missouri
"""
#load the libraries
import random as rm
import collections as cl

inputList = []
outputList = []
winCounter  = 0

eventR_After_S = 0
eventS_After_R = 0
eventS_After_P = 0
eventP_After_S = 0
eventP_After_R = 0
eventR_After_P = 0
eventP_After_P = 0
eventS_After_S = 0
eventR_After_R = 0

#calculate and return the probability#
def prob(a,b):
    return round((a/b),2)

#Bayesian Theorem probability function#
def probAgivenB(a,b,eventCount):
    inCnt = cl.Counter(inputList)
    countB = inCnt[b]
    totalCount = len(inputList)
    probB_and_A = prob(eventCount,totalCount)
    probB = prob(countB,totalCount)
    probA_given_B = round((probB_and_A/probB),2)
    return probA_given_B
  

if input == "": # initialize variables for the first round
    output1 = rm.choice(['P','S','R'])
else:
    inputList.append(input)
    n = len(inputList)
    if n > 2:
        last = inputList[-1]
        secondLast = inputList[-2]
        
        outputLast = outputList[-1]
        
        if(last == "R" and outputLast == "P"):
            winCounter += 1
        elif(last == "S" and outputLast == "R"):
            winCounter += 1
        elif(last == "P" and outputLast == "S"):
            winCounter += 1
        
        if(last == secondLast == "R"):
            eventR_After_R += 1
            output1 = "P"
        elif(last == secondLast == "P"):
            eventP_After_P += 1
            output1 = "S"
        elif(last == secondLast == "S"):
            eventS_After_S += 1
            output1 = "R"
        elif(secondLast == "R" and last == "P"):
            eventP_After_R += 1
            output1 = "S"
        elif(secondLast == "P" and last == "R"):
            eventR_After_P += 1
            output1 = "P"    
        elif(secondLast == "P" and last == "S"):
            eventS_After_P += 1
            output1 = "R"
        elif(secondLast == "S" and last == "P"):
            eventP_After_S += 1
            output1 = "S"
        elif(secondLast == "S" and last == "R"):
            eventR_After_S += 1 
            output1 = "P"
        elif(secondLast == "R" and last == "S"):
            eventS_After_R += 1
            output1 = "R"
        else:
            output1 = rm.choice(['P','S','R'])
            
        if(last == 'R'):
            probS_R = probAgivenB('S','R',eventR_After_S)
            probP_R = probAgivenB('P','R',eventR_After_P)
            probR_R = probAgivenB('R','R',eventR_After_R)
            #if max(probS_R,probP_R,probR_R) > 0.5:
            if((probS_R > probP_R) and (probS_R > probR_R)):
                output1 = "R"
            elif((probP_R > probS_R) and (probP_R > probR_R)):
                output1 = "S"
            elif((probR_R > probS_R) and (probR_R > probP_R)):
                output1 = "P"
        elif(last == 'P'):
            probS_P = probAgivenB('S','P',eventP_After_S)
            probP_P = probAgivenB('P','P',eventP_After_P)
            probR_P = probAgivenB('R','P',eventP_After_R)
            #if max(probS_P,probP_P,probR_P) > 0.5:
            if((probS_P > probP_P) and (probS_P > probR_P)):
                output1 = "R"
            elif((probP_P > probS_P) and (probP_P > probR_P)):
                output1 = "S"
            elif((probR_P > probS_P) and (probR_P > probP_P)):
                output1 = "P"
        elif(last == 'S'):
            probS_S = probAgivenB('S','S',eventS_After_S)
            probP_S = probAgivenB('P','S',eventS_After_P)
            probR_S = probAgivenB('R','S',eventS_After_R)
            #if max(probS_S,probP_S,probR_S) > 0.5:
            if((probS_S > probP_S) and (probS_S > probR_S)):
                output1 = "R"
            elif((probP_S > probS_S) and (probP_S > probR_S)):
                output1 = "S"
            elif((probR_S > probS_S) and (probR_S > probP_S)):
                output1 = "P"
    else:
        output1 = rm.choice(['P','S','R'])
        
outputList.append(output1)
#if winCounter >= 3400:
#    output1 = "S"

output = output1