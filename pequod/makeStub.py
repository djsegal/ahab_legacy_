# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:24:26 2013

@author: dan
"""

from   glob     import  glob
from   os       import  getcwd

def makeStub( curDir , numRuns ):
    
    # =================================
    #  make the condor submission stub
    # =================================
    
    condorStub = open( curDir + '/condorStub' , 'w' )
    
    condorStub.write('# ==================================  \n')
    condorStub.write('#  condor submission stub for bucky   \n')
    condorStub.write('# ==================================  \n\n')
    
    condorStub.write('input      = bucky.inp  \n')
    condorStub.write('executable = bucky_hdf  \n')
    condorStub.write('universe   = vanilla    \n')                     
    condorStub.write('error      = test.error \n')           
    condorStub.write('log        = test.log   \n\n')    

    condorStub.write('when_to_transfer_output = ON_EXIT_OR_EVICT \n')
    condorStub.write('should_transfer_files   = YES \n')
    condorStub.write('requirements            = OpSys == "LINUX" \n')
    condorStub.write('notification            = Error \n\n')       
   
   
    inputDir = getcwd() +  '/extraInput/'
    
    print glob(  inputDir +         "eos.*"  )
    condorStub.write('transfer_input_files = '   + inputDir +  'xraydat,'  
                           + ( ',' ).join(   glob( inputDir +    "eos.*"   ) 
                         ) +  '\n' )  
    
    strLen = len(str(numRuns))              
    for i in range(numRuns): 
        curStr = str(i).zfill(strLen)
        curInput  =  curDir + '/' + curStr
        condorStub.write( '\n' + 'initialdir = ' + curInput +
                          '\n' + 'queue    '     +  '\n'    )    
          
    condorStub.close()    