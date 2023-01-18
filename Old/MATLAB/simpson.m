function I = simpson(f, a, b, n)
%% Simpson integral
%% n = number of points

x = linspace(a, b, n);            
h = (b - a)/(n - 1);

I = h/3*(f(x(1)) + 4*sum(f(x(2:2:n-1))) + 2*sum(f(x(3:2:n-2))) + f(x(n)));

end
