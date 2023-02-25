[x,y]=ode45(@f,[0 3000],[2 0]);
plot(x,y(:,1))


function F = f(x, y)
    F = zeros(2, 1);
    F(1) = y(2);
    F(2) = -y(1) + 1000 * (1-y(1)^2) * y(2);
end