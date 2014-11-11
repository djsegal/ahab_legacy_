# -*- coding: utf-8 -*-
""" # *********************************************************************** #
Created on Mon Jul  1 01:31:22 2013

@author: dan segal (danSegal2@gmail.com)
""" # *********************************************************************** #
from   __future__                   import division
from   os                           import system

from   pequod.readInput             import readInput
from   pequod.getValueCombinations  import getValueCombinations
from   pequod.makeNewRunDir         import makeNewRunDir
from   pequod.makeBuckyInputs       import makeBuckyInputs
from   pequod.makeStub              import makeStub
#from   pequod.makeMap              import makeMap

class parameterSweep(object):

    # ===========================
    #  Variable USERS can change
    # ===========================

    verbose = True

    # -----------------
    #  read in red.inp 
    # -----------------

    ( varList , valuesList , vectorList ) = readInput('red.inp')

    # -------------------------------------------------
    #  get every combination of values from valuesList
    # -------------------------------------------------

    ( varList , comboList , comboTypes , comboInfo ) = \
        getValueCombinations( varList ,valuesList , vectorList )

    # -----------------------------------------------------        
    #  create a directory for every set defined by red.inp
    #    and fill them with their own modified bucky.inp
    # -----------------------------------------------------

    curDir = makeNewRunDir()
    makeBuckyInputs( curDir , varList , comboList )

    # ------------------------------------
    #  if verbose, print all the sublists
    # ------------------------------------    

    if verbose :
                
        print '\n   being verbose   \n'
        for              aList in comboList :   
            for        subList in     aList :   
                print  subList      
        
    # ---------------------------------------------     
    #  make condor stub and submit cluster of jobs
    # ---------------------------------------------    
            
    makeStub( curDir , len(comboList) )
    
    system( 'condor_submit ' + curDir + '/condorStub' )

    # ---------------------------------------------------------
    #  make an excel readable map of curDir and finish program
    # ---------------------------------------------------------

    #makeMap( curDir , varList , combinationList )
    
    print('\n ok done \n')
