a = 0;
b = 5;
h = 1;

if findstr(input('simp or trap: ', 's'), 'simp')
    tic
    disp(simpson(a, h, b))
    toc
else
    tic
    disp(trap(a, h, b))
    toc
end

function res = trap(a, h, b)
    res = 0;
    past_res = 1;

    % Пока разница между текущим значением и предыдущим больше е,
    % уменьшать шаг
    while abs(abs(res) - abs(past_res)) > 0.0001
        past_res = res;
        res = 0;
        for x = a:h:b
            res = res + 0.5*(f(x)+f(x+h))*h;
        end
        h = h / 10;
    end
end

function res = simpson(a, h, b)
    x1 = a+h:h*2:b-h;
    x2 = a+h*2:h*2:b-h*2;
    res = h / 3.0 * (f(a) + f(b) + 4 * sum(f(x1)) + 2 * sum(f(x2)));
end

function y = f(x)
    y = sin(x).*exp(-x);
end

