clear all; close all; clc;

% Spline example

f = @(x) 1./(1 + 25*x.^2);
X = linspace(-1, 1, 1000);
F = f(X);

figure;
g = 0;
for k = 5:10
    x = linspace(-1, 1, k+1);
    Fp = polyval(polyfit(x, f(x), k), X);
    g = g + 1;
    subplot(2,3,g), plot(x, f(x), '*', X,F,'k-', X, Fp,'r-'); grid on;
    title(['degree = ' num2str(k)]);
end