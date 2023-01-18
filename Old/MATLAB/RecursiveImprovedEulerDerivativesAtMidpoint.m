function [x, y] = RecursiveImprovedEulerDerivativesAtMidpoint(f, x0, xf, y0, n, Nr)
%% Improved Euler for 1st order ODE
%% n = number of points

h = (xf - x0)/(n - 1);
x = linspace(x0, xf, n);    
y = zeros(1, n);    

y(1) = y0;
for k = 1:n-1
    fm = f(x(k) + h/2, y(k) + h*f(x(k),y(k))/2);
    for r = 1:Nr
        fm = f(x(k) + h/2, y(k) + h*fm/2);
    end
    y(k + 1) = y(k) + h*fm;
end
