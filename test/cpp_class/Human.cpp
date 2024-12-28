#include "Human.h"
#include <sstream>
#include <iomanip>

Human::Human(const std::string& name, int age, double height, double weight)
  : name(name), age(age), height(height), weight(weight) {}

// Getters
std::string Human::getName() const {
    return name;
}

int Human::getAge() const {
    return age;
}

int Human::getHeight() const {
    return height;
}

int Human::getWeight() const {
    return weight;
}
// Setters
void Human::setName(const std::string& name) {
    this->name = name;
}

void Human::setAge(int age) {
    this->age = age;
}

void Human::setHeight(double height) {
    this->height = height;
}

void Human::setWeight(double weight) {
    this->weight = weight;
}

// Calculate BMI
double Human::calculateBMI() const {
    if (height > 0) {
        return weight / (height*height);
    }
    return 0.0;
}
