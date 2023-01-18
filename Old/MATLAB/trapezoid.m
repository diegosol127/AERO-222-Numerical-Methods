function I = trapezoid(f, a, b, n)
%% Trapezoid integral
%
%    f = function to integrate
% a, b = range of integration
%    n = number of partitions

x = linspace(a, b, n+1);
h = (b - a)/n;
I = (f(a)/2 + sum(f(x(2:n))) + f(b)/2)*h;

end
