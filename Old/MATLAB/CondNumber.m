clear; close all; clc;

A = [1, -1, 2; 3, 0, 1; 1, 0, 2];

AI = inv(A);

sigma = svd(A);

cond(A),
norm(A)
norm(AI),

max(sigma)
min(sigma)