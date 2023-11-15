#include <iostream>
#include <stdio.h>
#include <string.h>

class Shape {
public:
    double x, y;
    char * name;
    Shape(){
        x = y = 0;
        name = nullptr;
    }
    Shape(double x, double y, const char *name) : x(x), y(y) {
        this->x = x; this->y = y; this->name = new char[strlen(name)];
        for (int i = 0; i < strlen(name); i++){
            this->name[i] = name[i];
        }
    }

    Shape &operator=(const Shape& obj){
        this->x = obj.x; this->y = obj.y;
        delete [] this->name;
        size_t len = strlen(obj.name);
        this->name = new char[len];
        for (int i = 0; i < strlen(name); i++){
            this->name[i] = obj.name[i];
        }
    }

    ~Shape() {
        delete [] name;
    }
};

#include <cmath>

class Circle : public Shape {
public:
    double radius;

    Circle() : Shape(), radius(0) {}

    Circle(double x, double y, const char* name, double radius) : Shape(x, y, name), radius(radius) {}

    double area() const {
        return 3.141592 * radius * radius;
    }

    ~Circle() {}
};

class ColoredShape : public Circle {
public:
    std::string color;

    ColoredShape() : Circle(), color("") {}

    ColoredShape(double x, double y, const char* name, double radius, const std::string& color)
        : Circle(x, y, name, radius), color(color) {}

    ~ColoredShape() {}
};