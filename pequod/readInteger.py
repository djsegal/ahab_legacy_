# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:37:52 2013

@author: dan
"""
from __future__ import division


def readInteger( curMode , inpValues ) :

    if curMode == 1:            # init : increment : final
        
        curValues = [inpValues[0]]
        
        if ( inpValues[2] > inpValues[0] and inpValues[1] < 0 or
             inpValues[0] > inpValues[2] and inpValues[1] > 0 ):
                 inpValues[1] = -inpValues[1]     
        
        if ( inpValues[0] != inpValues[2] and inpValues[1] != 0 and
             abs(inpValues[0]  + inpValues[1])  <=  abs(inpValues[2]) ):
                 
            done = False
            while ( not done ):
                wrkValue = curValues[-1] + inpValues[1]

                # make sure the last value is inpValues[2]
                if abs(wrkValue) == abs(inpValues[2]):
                    curValues.append( inpValues[2] )
                    done = True
                elif abs(wrkValue)  > abs(inpValues[2]):
                    # if the last value of curValues is basically
                    # inpValues[2] (e.g. 99.9 ~= 100), set them equal
                    #
                    done = True
                else:
                    curValues.append( wrkValue )

        else:
            curValues = inpValues[0]
 
    elif curMode == 2:          # init , final     , numVals
        
        inpValues[2] = abs(inpValues[2])
        curValues = []
        
        if   inpValues[2]  > 1:
            for i in range(inpValues[2]):
                iTmp = ( i / (  ( inpValues[2] - 1 ) ) * 
                    ( inpValues[1] - inpValues[0] ) )
                curValues.append( inpValues[0] + iTmp )
        elif inpValues[2] == 1:
            curValues = inpValues[0]
            
    elif curMode == 3:          # init ; final     ; numVals
        
        inpValues[2] = abs(inpValues[2])
        curValues = []

        if   inpValues[2]  > 1:
            
            constFactor = pow(    (inpValues[1]/inpValues[0]) ,
                              1.0/( (inpValues[2]-     1      ) ) )

            curValues.append( inpValues[0] )                 
            for i in range(1,inpValues[2]-1):
                curValues.append( constFactor * curValues[-1] )
            curValues.append( inpValues[1] )
             
        elif inpValues[2] == 1:
            curValues = inpValues[0]
            
    elif curMode == 4:          # init | increment | numVals
        
        inpValues[2] = abs(inpValues[2])
        curValues = []
    
        if   inpValues[2]  > 1:
            for i in range(inpValues[2]):
                curValues.append( inpValues[0] + i * inpValues[1] )
        elif inpValues[2] == 1:
            curValues = inpValues[0]
        
    else:
        
        print('err with curMode: curMode = ')
        print(curMode)

    if not isinstance(curValues,list):
        curValues = [curValues]
        
    curValues = map(round,curValues)
    curValues = map( int ,curValues)
    
    returnValues = []
    
    for i in range(len(curValues)):
        if curValues[i] not in returnValues:
            returnValues.append(curValues[i])
        elif curMode > 1 and i != len(curValues): # i.e. the numVals criteria is not met
            modifiedVal = .5 * ( curValues[i-1] + curValues[i+1] )
            modifiedVal = int( round( modifiedVal ) )
            returnValues.append(modifiedVal)
    
    return returnValues
            