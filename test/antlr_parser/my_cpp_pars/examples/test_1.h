#ifndef HOLA
#define ADIOS

#include <string>
#include <iostream>

// First C++ class
class MyClass {
public:
    MyClass(int value);
    int getValue();
    void setValue(int v);
    
    // Static arithmetic operations
    static int sum(const MyClass& a, const MyClass& b);
    static int subtract(const MyClass& a, const MyClass& b);

private:
    int value;
}

// Second C++ class
//
// class AnotherClass {
// public:
//     AnotherClass(const char* text);
//     const char* getText() ;
//     void setText(const char* t);
//
// private:
//     std::string text;
// };
//
// // Standalone functions
// int double_value(const MyClass* obj);
// std::string combine_texts(const AnotherClass* obj1, const AnotherClass* obj2);

#endif // MY_CLASSES_H
