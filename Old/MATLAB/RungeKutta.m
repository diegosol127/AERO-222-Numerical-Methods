function [x, y] = RungeKutta(f, x0, xf, y0, n)

x = linspace(x0, xf, n); 
h = (xf - x0)/(n - 1); 
y = zeros(1, n);
y(1) = y0;
for k = 1:n-1
    k1 = h*f(x(k), y(k));
    k2 = h*f(x(k)+h/2, y(k)+k1/2);
    k3 = h*f(x(k)+h/2, y(k)+k2/2);
    k4 = h*f(x(k)+h, y(k)+k3);
    y(k+1) = y(k) + (k1 + 2*k2 + 2*k3 + k4)/6;
end

end