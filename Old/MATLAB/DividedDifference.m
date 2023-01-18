% Divided differences
clear; close all; clc;

X = [0.3, 1.0, 0.7, 0.6, 1.9]';
n = length(X);
P = zeros(n);
P(:,1) = 2*X.^3 - X.^2 + X - 1;
for c = 2:n
    for r = 1:n+1-c
        P(r,c) = (P(r+1,c-1) - P(r,c-1))/(X(c+r-1) - X(r));
    end
end
P,