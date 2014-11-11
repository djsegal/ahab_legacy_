% ===========================================
%  Matlab Part of Python-to-Matlab Converter
% ===========================================

disp '                                                  '
disp '=================================================='
disp '  Welcome to the Python-to-Matlab AHAB Converter  '
disp '=================================================='
disp '                                                  '

origFolder  =  pwd ;

curData  =  strsplit(  ls( 'data' )   )  ;

curData  =  curData(  ~cellfun( 'isempty' , curData )  )  ;

curData  =  sort( curData ) ;

disp ' Which directories have variables you wish to load? '
disp '                                                    '

curStr = '     ' ;

for i = 1 : length( curData )
              
    curStr = ': ' ;
    
    curStr = strcat(  num2str(i) , {' '} , curStr ,  {' '} , curData(i)  );
    
    disp( curStr{1} )
    
end

done = 0 ;  %  not done

while done == 0
   
    disp '                                         '
    curInp = input(' Enter Directory Numbers : ','s') ;
    
    curDir = str2num( curInp ) ;
    done = 1 ;
    
end

disp ' '

tmpDir = strcat(  origFolder  ,  '/data/'  ,  curData( curDir )  )  ; 

tmpDirContents = dir(  fullfile( tmpDir{1} , '*.mat' )  )  ;

tmpNames = { tmpDirContents.name } ;

for i = 1 : length( tmpNames ) 
       
    aTmpName     =  tmpNames(i) ;
    
    aTmpName     =  aTmpName{1} ;
    
    tmpFilename  =  strcat( tmpDir , '/' , aTmpName ) ;
    
    tmpVector =  load( tmpFilename{1} ) ;  
    
    tmpVector =  tmpVector ;
    
    tmpVector =  tmpVector(1).arr ;
            
    aTmpName  =  aTmpName(  1 : length( aTmpName ) - 4  )  ;
    
    curSplit  =  strsplit(  aTmpName , '_'  ) ;
    
    varName   =  curSplit(1) ;
    
    varName   =  varName{1} ;
    
    if length( curSplit ) == 3
       
        tmpNamePart = curSplit(2) ;
        
        varName = strcat( varName , '_' , tmpNamePart ) ;
        
        varName = varName{1} ;
        
    end
    
    %jobNum   =  curSplit(2) or curSplit(3)
    
    curEvalStr = strcat( 'exist(''' ,varName , ''',' , '''var''' , ')' ) ;
    
    varExists =  evalin('base', curEvalStr ) ;
        
    if varExists == 1
        
        preExistingVector = evalin( 'base' , varName ) ;
        
        tmpVector = cat( 1 , preExistingVector , tmpVector ) ;
        
    end
    
    assignin( 'base' , varName , tmpVector ) ;
    
    
end


%cd tmpFile%
%disp(tmpDirContents)

%dist(matchList)
