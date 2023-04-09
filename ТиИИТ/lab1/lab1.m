function [] = lab1(a,b,d)
    
    x = [a:d:b];
    for i = 1 : size(x,2)
        y(i) = 2*x(i)^3+1*x(i)^2+2*x(i)-6-15*sin(5*x(i));
        zero(i) = 0;
    end;
    plot(x,y,x,zero);
    
    
end;