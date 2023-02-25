a = [1 2;3 4];
b = cat(1, [5 6], [7 8]);

plus = a + b;
minus = b - a;
multiplication = a * b;

bar(plus)
bar(minus)
bar(multiplication)