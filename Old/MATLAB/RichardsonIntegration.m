clear; close all; clc;

%% Richardson extrapolation applied to trapezoid and Midpoint

f =@(x) exp(-x).*sin(3*x.^2);
a =-1;
b = 2;

n1 = 16;
n2 = 17;
h1 = (b - a)/n1;
h2 = (b - a)/n2;

%% Trapezoid and Midpoint accuracy h^p
p = 2;
format long

I1 = trapezoid(f, a, b, n1),
I2 = trapezoid(f, a, b, n2),

% x1 = linspace(a, b, n1+1);
% x2 = linspace(a, b, n2+1);
% plot(x1,f(x1),'k*',x2,f(x2),'rO'); grid on;
c = (I1 - I2)/(h2^p - h1^p),
IRE = I1 + c*h1^p,
%IRE = I2 + c*h2^p,

%% Richardson extrapolation applied to midpoint

I1 = midpoint(f, a, b, n1),
I2 = midpoint(f, a, b, n2),

% x1 = linspace(a, b, n1+1);
% x2 = linspace(a, b, n2+1);
% plot(x1,f(x1),'k*',x2,f(x2),'rO'); grid on;

c = (I1 - I2)/(h2^p - h1^p),
IRE = I1 + c*h1^p,
%IRE = I2 + c*h2^p,
