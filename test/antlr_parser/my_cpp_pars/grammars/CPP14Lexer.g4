lexer grammar CPP14Lexer;

// Keywords
Class:          'class';
Void:           'void';
PublicAccess:   'public';
ProtectedAccess:'protected';
PrivateAccess:  'private';
Ifndef:         'ifndef';
Define:         'define';
Endif:          'endif';
Include:        'include';

// Symbols
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
Static:         'static';
Const:          'const';
Ampersand:      '&';
Star:           '*';

// Types must come before Identifier to take precedence
Type
    : BuiltInType
    | Identifier (DoubleColon Identifier)*
    ;

fragment BuiltInType
    : 'bool' 
    | 'char' 
    | 'int' 
    | 'float' 
    | 'double' 
    | 'long' 
    | 'short'
    | 'string'
    ;

MacroIdentifier
    : [A-Z_] [A-Z0-9_]*
    ;

// Modified to handle different types of identifiers
Identifier
    : [a-zA-Z] [a-zA-Z0-9_]*  
    ;

// Skip whitespace and comments
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
