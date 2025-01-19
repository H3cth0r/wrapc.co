grammar CPP;

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
    : Hash Include LeftChevron Identifier (DoubleColon Identifier )* (Dot Identifier)? RightChevron
    ;

classDefinition
    : Class className classDerivation? LeftBrace classContent* RightBrace Semi?
    ;

className
    : Identifier
    ;
classDerivation
    : Colon (PublicAccess | ProtectedAccess | PrivateAccess) derivedClassName 
    ;
derivedClassName
    : Identifier
    ;

classContent
    : accessSpecifier
    | attributeDeclaration
    | Virtual? (methodDeclaration | constructorDeclaration | destructorDeclaration)
    ;

accessSpecifier
    : (PublicAccess | ProtectedAccess | PrivateAccess) Colon
    ;

methodDeclaration
    : templateStatement? methodReturnType methodName LeftPar parameterList? RightPar Const? ( Override | (Equal (Digit|Identifier))? ) Semi
    ;
templateStatement
    : Template LeftChevron Typename returnType RightChevron
    ;
methodReturnType
    : returnType
    ;
methodName
    : Identifier
    ;
constructorDeclaration
    : className LeftPar parameterList? RightPar Const? (Equal (Digit|Identifier))? Semi
    ;
destructorDeclaration
    : Tilde className LeftPar RightPar Const? (Equal (Digit|Identifier))? Semi
    ;

functionDefinition
    : functionReturnType Identifier LeftPar parameterList? RightPar Semi
    ;
functionReturnType
    : returnType
    ;

parameterType
    : returnType
    | className
    ;

attributeDeclaration
    : returnType Identifier Semi
    ;

returnType
    : (Static | Const)? ( Bool | Char | Int | Float | Double | Long | Short | Void | undefinedReturnType) (Ampersand | Star)?
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
    | Const? parameterType Identifier array
    ;

array
    : LeftBracket Digit? RightBracket
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
Virtual:        'virtual';
Override:       'override';
Template:       'template';
Typename:       'typename';

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
LeftBracket:    '[';
RightBracket:   ']';
LeftChevron:    '<';
RightChevron:   '>';
Semi:           ';';
Colon:          ':';
DoubleColon:    '::';
Comma:          ',';
Dot:            '.';
Hash:           '#';
Ampersand:      '&';
Star:           '*';
Tilde:          '~';
Equal:          '=';

Identifier
    : [a-zA-Z] [a-zA-Z0-9_]*  
    ;

Digit
    : [0-9]+
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
