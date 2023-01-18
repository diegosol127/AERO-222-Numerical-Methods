function I = Gauss_Legendre(f, a, b, x, w)

%% Gauss-Legendre integration

n = length(x);

I = 0;
for k = 1:n
    z = (x(k) + 1)*(b - a)/ 2 + a;
    I = I + w(k)*f(z);
end
I = I*(b - a)/2;

