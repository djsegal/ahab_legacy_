   # -*- coding: utf-8 -*-
"""
Created on Sat May 24 22:43:05 2014

The error messages used in ahab

@author: dan
"""


# not added yet

#------------------------------------------------------------------------------

err0   =  '                                                     \n\n'
err0  +=  '            Error: Invalid Increment Input             \n'
err0  +=  '            ******************************             \n' 
err0  +=  '            increment chars have to match              \n'
err0  +=  '            for example:  {1:2:3} is Good               \n'
err0  +=  '                          {1|2,3} is Bad                \n'

#------------------------------------------------------------------------------

err1   =  '                                                     \n\n'
err1  +=  '                Error: Mismatched Sets                 \n'
err1  +=  '            ******************************             \n' 
err1  +=  '   one of your sets has a member with the wrong size   \n'

#------------------------------------------------------------------------------

err2   =  '                                                     \n\n'
err2  +=  '                Error: `@(` Not Allowed                \n'
err2  +=  '            ******************************             \n' 
err2  +=  '         use something like @{ or @[ instead           \n'

#------------------------------------------------------------------------------

err3   =  '                                                     \n\n'
err3  +=  '            Error: Unbalanced Parentheses              \n'
err3  +=  '          *********************************            \n' 
err3  +=  '    match number of "(" and ")" inside every const     \n'

#------------------------------------------------------------------------------

err4   =  '                                                     \n\n'
err4  +=  '          Error: Parentheses No Longer Used            \n'
err4  +=  '        *************************************          \n' 
err4  +=  '   "(" and ")" no longer used for original purpose     \n'
err4  +=  '         Please remove this error message and          \n'
err4  +=  '           the try statement that calls it             \n'

#------------------------------------------------------------------------------

err5   =  '                                                     \n\n'
err5  +=  '    Error: Misspelled or Unregistered Constants        \n'
err5  +=  '   *********************************************       \n' 
err5  +=  '    check for typos every time consts are used         \n'
err5  +=  '      AND make sure every const is declared            \n'

#------------------------------------------------------------------------------

err6   =  '                                                     \n\n'
err6  +=  '              Error: Empty Vector Found                \n'
err6  +=  '            *****************************              \n' 
err6  +=  '                please find it  .and.                  \n'
err6  +=  '            ( fill it in .or. remove it )              \n'

#------------------------------------------------------------------------------

err7   =  '                                                     \n\n'
err7  +=  '              Error: No Variables Found                \n'
err7  +=  '          *********************************            \n' 
err7  +=  '           please add vars to red.inp file             \n'

#------------------------------------------------------------------------------
