function [x, y] = RecursiveImprovedEulerAverageDerivatives(f, x0, xf, y0, n, Nr)
%% Improved Euler for 1st order ODE
%% n = number of points

h = (xf - x0)/(n - 1);
x = linspace(x0, xf, n);     
y = zeros(1, n);    

y(1) = y0;
% for k = 1:n-1
%     fk = f(x(k), y(k));
%     fm = (fk + f(x(k + 1), y(k) + h*fk))/2;
%     for r = 1:Nr
%         fm = (fk + f(x(k + 1), y(k) + h*fm))/2;
%     end
%     y(k + 1) = y(k) + h*fm;
% end

for k = 1:n-1
    fk = f(x(k), y(k));
    ykp1 = y(k) + h*(fk + f(x(k+1), y(k) + h*fk))/2;
%    ykp1 = y(k) + h*(fk + f(x(k+1), ykp1))/2;
    y(k + 1) = y(k) + h*(fk + f(x(k+1), ykp1))/2;
end

