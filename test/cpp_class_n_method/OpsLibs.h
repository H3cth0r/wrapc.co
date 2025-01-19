#ifndef OPSLIB_H
#define OPSLIB_H

#include <string>

class Point {
    private:
      int x;
      int y;
    public:
      std::string name;

      Point(int x, int y, const std::string name);

      int getX() const;
      int getY() const;

      void moveOnXBy(int x);
      void moveOnYBy(int y);
};

double calculateAverage(const int arr[], int size) ;

double sum_cpp(int aa, int bb);

#endif
