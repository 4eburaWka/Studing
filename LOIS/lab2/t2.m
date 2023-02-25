m = menu('Выберите вариант:','K = 0','K = 0.01');

if m == 2
    disp('K = 0.01')
    K = 0.01;
    [x, y] = ode45(@f2,[0 20], [0 1]);
    plot(x, y(:, 1), x, y(:, 2))
else
    disp('K = 0')
    K = 0;
    [x, y] = ode45(@f1,[0 20], [0 1]);
    plot(x, y(:, 1), x, y(:, 2))
end




function F = f1(x, y)
    F = zeros(2, 1);

    F(1) = (0 * (x * x) + y(2));
    F(2) = -y(1);
end

function F = f2(x, y)
    global K;
    F = zeros(2, 1);

    F(1) = (0.01 * (x * x) + y(2));
    F(2) = -y(1);
end