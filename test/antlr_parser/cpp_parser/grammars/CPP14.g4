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
    : returnType Identifier LeftPar parameterList? RightPar Semi
    ;
constructorDeclaration
    : className LeftPar parameterList? RightPar Semi
    ;

returnType
    : Bool
    | Char
    | Int
    | Float 
    | Double
    | Long 
    | Short
    | String
    | Void
    ;

parameterList
    : parameter (Comma parameter)*
    ;

parameter
    : Const? parameterType Identifier
    | Const? parameterType Ampersand Identifier
    | Const? parameterType Star Identifier
    ;

parameterType
    : Type
    | className
    ;

attributeDeclaration
    : returnType Identifier Semi
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
String:   'string';
    

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

Type 
    : Identifier (DoubleColon Identifier)*
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
