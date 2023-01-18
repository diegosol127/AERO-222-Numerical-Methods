function [x, y] = ImprovedEulerDerivativesAtMidpoint(f, x0, y0, h, n)
%% Improved Euler for 1st order ODE
%% h = step
%% n = number of steps

x = zeros(1, n+1);    
y = zeros(1, n+1);    

x(1) = x0;
y(1) = y0;
for k = 1:n
    fk = f(x(k), y(k));
    y(k + 1) = y(k) + h*f(x(k) + h/2, y(k) + h/2*fk);
    x(k + 1) = x(k) + h;
end
