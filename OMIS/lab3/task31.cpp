#include <iostream>

class Shape {
public:
    double x, y;

    Shape(double x, double y) : x(x), y(y) {}

    void print() {
        std::cout << "Shape at (" << x << ", " << y << ")" << std::endl;
    }
};

class Circle : public Shape {
public:
    double radius;

    Circle(double x, double y, double radius) : Shape(x, y), radius(radius) {}

    void print() {
        std::cout << "Circle at (" << x << ", " << y << ") with radius " << radius << std::endl;
    }
};

int main() {
    Shape shape(1.0, 2.0);
    Circle circle(3.0, 4.0, 5.0);

    Shape* shapePtr = &shape;
    Shape* circlePtr = &circle;

    shapePtr->print();
    circlePtr->print();

    return 0;
}
