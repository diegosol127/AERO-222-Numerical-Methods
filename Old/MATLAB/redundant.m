clear all; close all; clc;

A = [1, -2 3; 2, 4, -1; -1, -14, 11];

x = linspace(-10, 10, 100);
y = linspace(-10, 10, 100);
z = linspace(-10, 10, 100);

xp = A(1,1)*x + A(1,2)*y + A(1,3)*z;
yp = A(2,1)*x + A(2,2)*y + A(2,3)*z;
zp = A(3,1)*x + A(3,2)*y + A(3,3)*z;

plot3(xp,yp,zp,'*'); grid on;