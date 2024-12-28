#ifndef HUMAN_H
#define HUMAN_H

#include <string>

class Human {
    private:
        std::string name;
        int age;
        double height;
        double weight;
      public:
        Human(const std::string& name, int age, double height, double weight);

        // Getters
        std::string getName() const;
        int getAge() const;
        double getHeight() const;
        double getWeight() const;

        // Setters
        void setName(const std::string& name);
        void setAge(int age);
        void setHeight(double height);
        void setWeight(double weight);

        // Functionality
        double calculateBMI() const;
};

#endif
