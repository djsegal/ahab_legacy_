# -*- coding: utf-8 -*-
""" # *********************************************************************** #
Created on Fri May 23 01:31:22 2014

a low-throughput computing hack-up of parameterSweep 
    that allows you to run a flock of seagulls on your own computer.

@author: dan segal (danSegal2@gmail.com)
""" # *********************************************************************** #
from   __future__                   import division
from   os                           import system , remove , chmod , chdir , getcwd , listdir , path
from   shutil                       import copyfile
from   re                           import search

from   pequod.readInput             import readInput
from   pequod.getValueCombinations  import getValueCombinations
from   pequod.makeNewRunDir         import makeNewRunDir
from   pequod.makeBuckyInputs       import makeBuckyInputs

#from   pequod.makeMap              import makeMap

class seagull(object):

    tagName  =  'seagull.tag' # signal that something's fishy
    verbose  =  False #True
    
    origDir  =  getcwd()
    tmpDir   = 'extraInput/' 
    
    # ===============================================
    #  Restarting a Run (and Possibly Abandoning it)
    # ===============================================

    if path.isfile(tagName):                
        
        with open( tagName , 'r' ) as thisTag:
            
            ( curDir , numRuns , curInd ) = thisTag.readlines()
            curDir  = curDir[0:-1]   # get rid of \n(ewline) operator
            numRuns = int(numRuns[0:-1])   # cast as int
            curInd  = int(curInd )   # cast as int

        if curInd == -1 or curInd == numRuns :
            
            for f in listdir( tmpDir ):
                
                if search( r'\Axraydat' , f ):
                    
                    continue
                
                if not search( r'\Aeos' , f ):
                    
                    remove(path.join(tmpDir, f))

            remove( tagName )

    # ======================== 
    #  Standard Run Procedure
    # ========================

    if not path.isfile(tagName):            
        
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
        #   and fill them with their own modified bucky.inp
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
                

        # ------------------------------------------------------------
        #
        #  put bucky.inp, bucky_hdf, bucky.h5, etc. inside extraInput
        #
        # ------------------------------------------------------------
        #
        #       + therefore, need to make a seagull tag, to indentify
        #               the flock in case something bad happens,
        #               such as the computer running it crashing
        #
        #       + the reason extraInput is the best spot to put  
        #               everything is b/c there are more eos 
        #               files than any other type of files
        #   
        #       + obviously, all of seagull is a pretty big hack.
        #               that dan segal sure isn't, though
        #               i hear he's a pretty swell guy
        #
        # ------------------------------------------------------------
    
        curInd  = 0 # start at beginning    
        numRuns = len(comboList)
    
        copyfile( 'bucky_hdf' , tmpDir + 'bucky_hdf' )

        chmod( tmpDir + 'bucky_hdf' , 0o777 )

        with open( tagName , 'w' ) as thisTag:  # leave initial tag
            thisTag.write( curDir + "\n" + str(numRuns-1) + "\n" + str(-1) )

    # -----------------------------  
    #  loop over all possible jobs
    # -----------------------------    
    
    strLen = len(  str( numRuns )  )
    
    for i in range( curInd , numRuns ) :  

        curRun  = curDir + '/' + str(i).zfill(strLen) + '/'
        
        copyfile( curRun + 'bucky.inp' , tmpDir + 'bucky.inp' )
        
        chdir( tmpDir )
        system( './bucky_hdf' )
        chdir( origDir )
        
        copyfile( tmpDir + 'bucky.h5'   , curRun + 'bucky.h5'  ) 
        copyfile( tmpDir + 'bucky.out'  , curRun + 'bucky.out'  )   

        with open( tagName , 'w' ) as thisTag:
            thisTag.write( curDir + "\n" + str(numRuns-1) + "\n" + str(i) )   
    
    # =================
    #  wrap-up program
    # =================

    for f in listdir( tmpDir ):
        
        # ---------------------------------------------------
        #  dont delete 'xraydat' (could add more files here)
        # ---------------------------------------------------
        
        if search( r'\Axraydat' , f ):
            
            continue
        
        # ----------------------------------------------
        #  delete every file that doesnt start with eos
        # ----------------------------------------------
        
        if not search( r'\Aeos' , f ):
            
            remove(path.join(tmpDir, f))

    remove( tagName )
    
    print('\n ok done \n')
