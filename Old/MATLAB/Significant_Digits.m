clear; close all; clc;

% x = input('Input a number = ');
% s = input('Significant digits = ');
format long;
x = pi;
for s = 2:12
    n = floor(log10(x)) - s + 1;
    v = round(x*10^(-n))*10^n;
    sprintf('%3.0f %12.9f\n', s, v)
%    disp(['SD = ' num2str(s) ' --> \pi = ' num2str(v)]);
end
