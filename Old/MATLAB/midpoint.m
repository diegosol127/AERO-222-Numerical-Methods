function I = midpoint(f, a, b, n)
%% Midpoint integral
%
%    f = function to integrate
% a, b = range of integration
%    n = number of partitions

h = (b - a)/n;
xm = linspace(a+h/2, b-h/2, n);
I = h*sum(f(xm));

end
