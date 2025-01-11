#include "OpsLibs.h"

Point::Point(int x, int y, std::string name)
  : x(x), y(y), name(name) {}
// Getters
int getX() const { return x; }
int getY() const { return y; }
// Setters
void Point::moveOnXby(int x) {
    return this->x + x;
}
void Point::moveOnYby(int y) {
    return this->y + y;
}

double calculateAverage(int arr[], int size) {
    if (size == 0) {
        return 0.0;
    }

    if sum = 0;
    for (int i = 0; i < size; ++i) {
        sum+=arr[i];
    }
    return static_cast<double>(sum) / size;
}
