#include <iostream>

class Shape {
public:
    Shape(double x, double y) : x(x), y(y) {
        std::cout << "Shape constructor called" << std::endl;
    }

    virtual double area() const = 0; // Чисто виртуальная функция для вычисления площади
    virtual void print() const {
        std::cout << "Shape at (" << x << ", " << y << ")" << std::endl;
    }

    virtual ~Shape() {
        std::cout << "Shape destructor called" << std::endl;
    }

protected:
    double x, y;
};

class Circle : public Shape {
public:
    Circle(double x, double y, double radius) : Shape(x, y), radius(radius) {
        std::cout << "Circle constructor called" << std::endl;
    }

    double area() const override {
        return 3.141592 * radius * radius;
    }

    void print() const override {
        std::cout << "Circle at (" << x << ", " << y << ") with radius " << radius << std::endl;
    }

    ~Circle() {
        std::cout << "Circle destructor called" << std::endl;
    }

private:
    double radius;
};

class Rectangle : public Shape {
public:
    Rectangle(double x, double y, double width, double height) : Shape(x, y), width(width), height(height) {
        std::cout << "Rectangle constructor called" << std::endl;
    }

    double area() const override {
        return width * height;
    }

    void print() const override {
        std::cout << "Rectangle at (" << x << ", " << y << ") with width " << width << " and height " << height << std::endl;
    }

    void setDimensions(double newWidth, double newHeight) {
        width = newWidth;
        height = newHeight;
    }

    ~Rectangle() {
        std::cout << "Rectangle destructor called" << std::endl;
    }

private:
    double width, height;
};

class ColoredShape : public Circle, public Rectangle {
public:
    ColoredShape(double x, double y, double radius, double width, double height, const std::string& color)
        : Circle(x, y, radius), Rectangle(x, y, width, height), color(color) {
        std::cout << "ColoredShape constructor called" << std::endl;
    }

    void print() const override {
        std::cout << "ColoredShape at (" << x << ", " << y << ") with color " << color << std::endl;
    }

    ~ColoredShape() {
        std::cout << "ColoredShape destructor called" << std::endl;
    }

private:
    std::string color;
};
