X = -100:1:100;
a1 = 15;
a2 = -10;
b1 = 0.04;
b2 = -0.05;
c1 = 0.05;
c2 = -0.03;
k1 = 0.7;
k2 = -0.1;
disp('x         z0')
alpha1 = 0;
alpha2 = 0;
zet1 = 0;
zet2 = 0;
arraya1 = [];
arraya2 = [];
arrayz0 = [];
for x = -100:1:100
    alpha1 = sigmFunc(a1, b1, x);
    alpha2 = sigmFunc(a2, b2, x);
    zet1 = linFuncRevers(c1, k1, alpha1);
    zet2 = linFuncRevers(c2, k2, alpha2);
    z0 = (alpha1 * zet1 + alpha2 * zet2) / (alpha1 + alpha2);
    arrayz0(end + 1) = z0;
    arraya1(end + 1) = alpha1;
    arraya2(end + 1) = alpha2;
    disp([x "        " z0])
end
plot(-100:1:100,arraya1)
hold on
plot(-100:1:100,arraya2)
plot(-100:1:100,arrayz0)


function z = linFuncRevers(c, k, a)
    z = (a - k) / c;
end


function alpha = sigmFunc(a, b, x)
    alpha = 1 / (1 + exp(1).^ (b.* (x - a)));
end
