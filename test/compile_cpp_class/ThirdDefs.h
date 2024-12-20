#ifndef ANIMAL_H
#define ANIMAL_H

#include <string>
#include <vector>
#include <memory>
#include <Python.h>

// Base class with virtual functions
class Animal {
public:
    virtual ~Animal() = default;

    // Pure virtual function to enforce implementation in derived classes
    virtual std::string speak() const = 0;

    // Virtual function with a default implementation
    virtual int getAge() const;

    // Function to set the age
    void setAge(int a);

protected:
    int age; // Protected member variable for age
};

// Derived class representing a Dog
class Dog : public Animal {
public:
    // Constructor to initialize the Dog's name and age
    Dog(const std::string& name, int age);

    // Implementation of the speak function
    std::string speak() const override;

    // Getter for the dog's name
    const std::string& getName() const;

    // Template method to calculate age in different units
    template<typename T>
    T getAgeInDifferentUnit(T multiplier) const;
    // T getAgeInDifferentUnit(T multiplier) const {
    //     return static_cast<T>(getAge()) * multiplier;
    // }

private:
    std::string name; // Private member variable for the dog's name
};

#endif // ANIMAL_H
