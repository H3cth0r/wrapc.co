#include "OpsLibs.h"

Point::Point(int x, int y, std::string name)
  : x(x), y(y), name(name) {}
// Getters
int Point::getX() const { return x; }
int Point::getY() const { return y; }
// Setters
void Point::moveOnXBy(int x) {
    this->x += x;
}
void Point::moveOnYBy(int y) {
    this->y += y;
}

double calculateAverage(int arr[], int size) {
    if (size == 0) {
        return 0.0;
    }

    int sum = 0;
    for (int i = 0; i < size; ++i) {
        sum+=arr[i];
    }
    return static_cast<double>(sum) / size;
}

double sum_cpp(int aa, int bb) {
  return aa + bb;
}
