#include "ThirdDefs.h"
// Animal class implementation
Animal::Animal() : age(0) {}

int Animal::getAge() const {
    return age;
}

void Animal::setAge(int a) {
    age = a;
}

// Dog class implementation
Dog::Dog(const std::string& name, int age) : name(name) {
    setAge(age);  // Using the base class method to set age
}

std::string Dog::speak() const {
    return "Woof!";
}

const std::string& Dog::getName() const {
    return name;
}

int Dog::getAgeInDifferentUnit(int multiplier) const {
    return getAge() * multiplier;
}
