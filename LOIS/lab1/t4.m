x0 = pi / 2;

x = fzero('func', x0)
y = func(x)

x = 0:0.0001:pi/2;
y = func(x);
plot(x,y)
