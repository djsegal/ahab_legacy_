# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:28:43 2013

@author: dan
"""

def makeMap( curDir , varList , valueCombinations ):
    
    # ================================================
    #  make a text document that contains the list of
    #   variable values found in all the condor jobs
    # ================================================

    mapFile = curDir + '/' + 'condorMap.txt'
    condorMap = open(mapFile, 'w')
    
    #  title row
    # -----------
    condorMap.write('job#' + ' ')
    for var in varList:
        condorMap.write( str(var) + ' ' )
    
    #  data rows
    # -----------    
    for i in range(len(valueCombinations)):  
        condorMap.write( '\n' )
        condorMap.write( str(i)  + ' ' )
        for j in range(len(valueCombinations[i])):  
            condorMap.write( str(valueCombinations[i][j]) + ' ' )
              
    condorMap.close()
