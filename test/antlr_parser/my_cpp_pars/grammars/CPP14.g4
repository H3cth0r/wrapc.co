grammar CPP14;

// Parser
program
    : openGuardian? programContent* closeGuardian?
    ;

openGuardian
    : Hash Ifndef Identifier Hash Define Identifier
    ;

closeGuardian
    : Hash Endif
    ;

programContent
    : includeStatement 
    | classDefinition 
    | functionDefinition 
    ;

includeStatement
    : Hash Include LeftChevron Identifier (DoubleColon Identifier)* RightChevron
    ;

classDefinition
    : Class className LeftBrace classContent* RightBrace Semi?
    ;

className
    : Identifier
    ;

classContent
    : accessSpecifier
    | methodDeclaration
    | constructorDeclaration
    | attributeDeclaration
    ;

accessSpecifier
    : (PublicAccess | ProtectedAccess | PrivateAccess) Colon
    ;

methodDeclaration
    : (Static | Const)? returnType Identifier LeftPar parameterList? RightPar Semi
    ;
constructorDeclaration
    : className LeftPar parameterList? RightPar Semi
    ;

functionDefinition
    : returnType Identifier LeftPar parameterList? RightPar Semi
    ;

parameterType
    : returnType
    | className
    ;

attributeDeclaration
    : returnType Identifier Semi
    ;

returnType
    : ( Bool | Char | Int | Float | Double | Long | Short | Void | undefinedReturnType) (Ampersand | Star)?
    ;

undefinedReturnType
    : Identifier (DoubleColon Identifier)*
    ;

parameterList
    : parameter (Comma parameter)*
    ;

parameter
    : Const? parameterType Identifier
    | Const? parameterType Ampersand Identifier
    | Const? parameterType Star Identifier
    ;


// Lexer
Class:          'class';
Void:           'void';
PublicAccess:   'public';
ProtectedAccess:'protected';
PrivateAccess:  'private';
Ifndef:         'ifndef';
Define:         'define';
Endif:          'endif';
Include:        'include';

Static:         'static';
Const:          'const';

Bool:     'bool';
Char:     'char';
Int:      'int';
Float:    'float';
Double:   'double';
Long:     'long';
Short:    'short';
    

LeftBrace:      '{';
RightBrace:     '}';
LeftPar:        '(';
RightPar:       ')';
LeftChevron:    '<';
RightChevron:   '>';
Semi:           ';';
Colon:          ':';
DoubleColon:    '::';
Comma:          ',';
Hash:           '#';
Ampersand:      '&';
Star:           '*';

Identifier
    : [a-zA-Z] [a-zA-Z0-9_]*  
    ;

Whitespace
    : [ \t]+ -> skip
    ;

Newline
    : ('\r' '\n'? | '\n') -> skip
    ;

BlockComment
    : '/*' .*? '*/' -> skip
    ;

LineComment
    : '//' ~[\r\n]* -> skip
    ;
