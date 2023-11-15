#include <iostream>
#include <vector>

// Базовый класс для точек
class Point {
public:
    double x, y;

    Point(double x, double y) : x(x), y(y) {}

    void print() const {
        std::cout << "Point at (" << x << ", " << y << ")" << std::endl;
    }
};

// Класс для линии, состоящей из двух точек
class Line {
public:
    Point start, end;

    Line(const Point& start, const Point& end) : start(start), end(end) {}

    void print() const {
        std::cout << "Line from (" << start.x << ", " << start.y << ") to (" << end.x << ", " << end.y << ")" << std::endl;
    }
};

// Класс для прямоугольника, заданного двумя диагональными угловыми точками
class Rectangle {
public:
    Point topLeft, bottomRight;

    Rectangle(const Point& topLeft, const Point& bottomRight) : topLeft(topLeft), bottomRight(bottomRight) {}

    void print() const {
        std::cout << "Rectangle from (" << topLeft.x << ", " << topLeft.y << ") to ("
                  << bottomRight.x << ", " << bottomRight.y << ")" << std::endl;
    }
};

// Класс, представляющий собой коллекцию фигур
class Drawing {
public:
    std::vector<Point> points;
    std::vector<Line> lines;
    std::vector<Rectangle> rectangles;

    void print() const {
        std::cout << "Drawing contains:" << std::endl;
        for (const auto& point : points) {
            point.print();
        }
        for (const auto& line : lines) {
            line.print();
        }
        for (const auto& rectangle : rectangles) {
            rectangle.print();
        }
    }
};

int main() {
    // Пример использования иерархии классов
    Point p1(1.0, 2.0);
    Point p2(3.0, 4.0);
    Line line(p1, p2);
    Rectangle rect(p1, p2);

    // Пример использования агрегации (Drawing содержит векторы фигур)
    Drawing drawing;
    drawing.points.push_back(p1);
    drawing.points.push_back(p2);
    drawing.lines.push_back(line);
    drawing.rectangles.push_back(rect);

    // Выводим содержимое рисунка
    drawing.print();

    return 0;
}
