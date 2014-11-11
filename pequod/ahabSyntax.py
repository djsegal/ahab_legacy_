# -*- coding: utf-8 -*-
"""
Created on Sat May 24 22:43:05 2014

The syntax used in ahab

@author: dan
"""

# From Original Input File: (needs update)

# !=============================================================================
#
#     -----------------
#	|   comment chars   |
#     -----------------
#	
#	+	the following are comment chars     :     !  ,  #  ,  %
#
#	+	comments have to be the first characters in lines         
#
#     -----------------
#	|   other   chars   |
#     -----------------
#
#    [      ]  -  vector
#   [[      ]] -  2D matrix
#    <      >  -  indep list to sweep over
# 
#   + - / * ^  -  math operations used for constants
# 
#    ..& &..   -  vector variation (set var to this or that)
# 
#    ! # $ %   -  comments
#    {} <> \\  -  sets        
#    '' "" ``  -  sets        
#              -  typed out list of varibles
#      | |     -  init | inc | numVals 
#    &{ @{ m_( -  something
#    $( $< $[  -  special utility (i.e. making targets)
#
# !=============================================================================
#
#             ---------------------
#				Value  Assignment
#             ---------------------
#
# 		init 	: 	increment   :   final
# 		init 	, 	final       ,   numVals     ( lin )
# 		init 	; 	final       ;   numVals     ( log )
# 		init 	| 	increment   |   numVals
#
# !=============================================================================
#
#------------------------------------------------------------------------------
#
# this stuff is gonna have to be added lated with re syntax parsing
#
#------------------------------------------------------------------------------
#
#   )*n }*n   -  repeat this line n times (makes the n independents part of a depend)
#   )^n }^n   -  repeat this line n times (makes the n independents part of a depend)
#
#------------------------------------------------------------------------------


# $============================================================================
#
#                           syntax lists below here
#
# $============================================================================


openingChars     =  (  [ '(' ]  +  [ '{' ]  +  [ '?' , '$' , '\\' ] + 
                       [ "'" , '`' , '"' ]  +  [ '~' ]  +  [  '<' ] )

closingChars     =  (  [ ')' ]  +  [ '}' ]  +  [ '?' , '$' , '\\' ] + 
                       [ "'" , '`' , '"' ]  +  [ '~' ]  +  [  '>' ] )

# -----------------------------------------------------------------------------

pythonMetaChars  =  [ '.' , '^' , '*' , '+'    , '?' , '$' , '\\' ,
                    
                      '{' , '}' , '[' , ']'    , '(' , ')' ,  '|' ]

# -----------------------------------------------------------------------------                      

pythonMathChars  =  [ '+' , '-' , '/' , '*' , '^' ]  
 
incrementChars   =  [ ':' , ',' , ';' , '|' ]

commentChars     =  [ '!' , '#' , '%' ]

floatChars	     =  [ '.' , 'e' , 'E' ]

#matrixChars     =  [  '[['  ,  ']]'  ]

vectorChars      =  [ '[' , ']' ]

# -----------------------------------------------------------------------------

constChar        =    '@'

andChar          =    '&'

equalChar        =    '='

inlineChar       =    "'"

pythonEscChar    =    '\\'

# -----------------------------------------------------------------------------

pythonMathWords  =  [   'sqrt('  ,
                         'sin('  ,    'cos('  ,    'tan('  ,
                         'exp('  ,    'log('  ,    'int('  , 
                        'ceil('  ,  'round('  ,  'floor('  ]

            