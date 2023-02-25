fminbnd('func2', 0.5, 1.0)
x = 0:0.01:3;
y = func2(x);
plot(x,y)


[x, fval] = fminsearch('func3', [1, 1])