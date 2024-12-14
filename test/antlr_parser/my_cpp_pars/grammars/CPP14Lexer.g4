lexer grammar CPP14Lexer;


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
