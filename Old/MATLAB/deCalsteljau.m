%% De Calsteljau Algorithm
chiudi;

%% control points
n = 4;
X = rand(1, n); x = X;
Y = rand(1, n); y = Y;
plot(X, Y, 'k-'); hold on;
t = 0.3; umt = 1-t;

x = x(1:3)*umt + x(2:4)*t;
y = y(1:3)*umt + y(2:4)*t;
plot(x, y, 'b-');
x = [X(1) x];
y = [Y(1) y];

x = x(1:2)*umt + x(2:3)*t;
y = y(1:2)*umt + y(2:3)*t;
plot(x, y, 'r-');
x = [X(1) x];
y = [Y(1) y];

x = x(1:1)*umt + x(2:2)*t;
y = y(1:1)*umt + y(2:2)*t;
plot(x, y, 'r*');
return,

t = linspace(0, 1, 1000);
t1 = (1 - t).^3; t2 = 3*t.*(1-t).^2; t3 = 3*(1-t).*t.^2; t4 = t.^3;
xb = X(1)*t1 + X(2)*t2 + X(3)*t3 + X(4)*t4;
yb = Y(1)*t1 + Y(2)*t2 + Y(3)*t3 + Y(4)*t4;
plot(xb, yb, 'r-'); grid on

