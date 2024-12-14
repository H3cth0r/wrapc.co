parser grammar CPP14Parser;
options {
    tokenVocab = CPP14Lexer;
}

cppFile
    : openGuardian programContent* closeGuardian?
    ;

openGuardian
    : Hash Ifndef MacroIdentifier
      Hash Define MacroIdentifier
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
    | constructorDeclaration
    | methodDeclaration
    | attributeDeclaration
    ;

accessSpecifier
    : (PublicAccess | ProtectedAccess | PrivateAccess) Colon
    ;

constructorDeclaration
    : className LeftPar parameterList? RightPar Semi
    ;

methodDeclaration
    : Static? returnType Identifier LeftPar parameterList? RightPar Semi
    ;

returnType
    : Type
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
    : Type Identifier Semi
    ;
