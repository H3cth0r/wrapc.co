parser grammar CPP14Parser;
options {
    tokenVocab = CPP14Lexer;
}

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
