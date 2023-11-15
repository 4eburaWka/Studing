#include <iostream>
#include <vector>
#include <cstring>

class Shape {
public:
    double x, y;
    char* name;

    Shape(double x, double y, const char* name) : x(x), y(y) {
        this->name = new char[strlen(name) + 1];
        strcpy(this->name, name);
    }

    void print() const {
        std::cout << "Shape at (" << x << ", " << y << ") with name: " << name << std::endl;
    }

    ~Shape() {
        delete[] name;
    }
};

class Circle : public Shape {
public:
    double radius;

    Circle(double x, double y, const char* name, double radius) : Shape(x, y, name), radius(radius) {}

    void print() const {
        std::cout << "Circle at (" << x << ", " << y << ") with name: " << name << " and radius " << radius << std::endl;
    }
};

int main() {
    std::vector<Shape*> shapes;

    char choice;

    do {
        std::cout << "Menu:" << std::endl;
        std::cout << "1. Add a Shape" << std::endl;
        std::cout << "2. Add a Circle" << std::endl;
        std::cout << "3. Print all shapes" << std::endl;
        std::cout << "4. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case '1': {
                double x, y;
                char name[100];
                std::cout << "Enter x and y coordinates: ";
                std::cin >> x >> y;
                std::cout << "Enter name: ";
                std::cin >> name;
                shapes.push_back(new Shape(x, y, name));
                break;
            }
            case '2': {
                double x, y, radius;
                char name[100];
                std::cout << "Enter x and y coordinates: ";
                std::cin >> x >> y;
                std::cout << "Enter name: ";
                std::cin >> name;
                std::cout << "Enter radius: ";
                std::cin >> radius;
                shapes.push_back(new Circle(x, y, name, radius));
                break;
            }
            case '3':
                for (const auto& shape : shapes) {
                    shape->print();
                }
                break;
            case '4':
                // Clean up allocated memory
                for (const auto& shape : shapes) {
                    delete shape;
                }
                break;
            default:
                std::cout << "Invalid choice. Try again." << std::endl;
        }
    } while (choice != '4');

    return 0;
}
