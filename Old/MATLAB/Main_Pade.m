clear; close all; clc;

%% MainPade'

%f = @(x,n) cat(2, log(1 - x), -factorial(n(2:end)-1)./((1-x).^n(2:end)));
f = @(x) exp(x);

[p, q] = pade(f, 0, 6, 6);
x = linspace(0, 1, 30);
%plot(x, log(1 - x), 'k-', x, polyval(p, x)./polyval(q, x),'rO'); grid on;
plot(x, exp(x), 'k-', x, polyval(p, x)./polyval(q, x),'rO'); grid on;

