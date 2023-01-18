clear; close all; clc;
set(0,'defaultTextInterpreter','latex');
figure('DefaultAxesFontSize',16)


%% Main improved Euler for first-order ODE

f =@(x,y) -2*y + x^3*exp(-2*x);

yt =@(x) (x.^4 + 4)/4.*exp(-2*x);
x0 = 0;
y0 = 1;
xf = 10;
n = 100;

[x, y] = ImprovedEulerAverageDerivatives(f, x0, xf, y0, n);
subplot(221); plot(x,y,'k-',x,yt(x),'r-'); grid on;
xlabel('$x$'); ylabel('$y$'); legend('Average','True');
subplot(223); plot(x,y-yt(x),'r-'); grid on;
xlabel('$x$'); ylabel('Average error');

[x, y] = ImprovedEulerDerivativesAtMidpoint(f, x0, xf, y0, n);
subplot(222); plot(x,y,'k-',x,yt(x),'r-'); grid on;
xlabel('$x$'); ylabel('$y$'); legend('Midpoint','True');
subplot(224); plot(x,y-yt(x),'r-'); grid on;
xlabel('$x$'); ylabel('Midpoint error');

