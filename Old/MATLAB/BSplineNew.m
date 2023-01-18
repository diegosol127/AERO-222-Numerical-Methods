clear all; close all; clc;
%% B-Spline Curves

N = 100;
u = linspace(0, 2, N);
u2 = u.*u;
u3 = u2.*u;
b1 = 1/6*(1 - u).^3;
b2 = u3/2 - u2 + 2/3;
b3 = (-u3 + u2 + u + 1/3)/2;
b4 = u3/6;

% figure(2);
% plot(u, [b1; b2; b3; b4]','-','LineWidth', 3); xlabel('u');
% grid on; legend('b_{-1}','b_0','b_1','b_2');

%% Control points
n = 12; x = rand(1, n); y = rand(1, n);

% x = [10 50 75 95  85  80];
% y = [10 15 60 100 140 180];

% [x, I] = sort(x);
% y = y(I);

n = length(x);

figure(1);
plot(x, y, 'k*'); grid on; xlabel('x'); ylabel('y'); hold on;
for k = 1:n, text(x(k)+0.01, y(k)+0.01, num2str(k)); end

%% Plots
for k = 1:n-3
    X = b1*x(k) + b2*x(k+1) + b3*x(k+2) + b4*x(k+3);
    Y = b1*y(k) + b2*y(k+1) + b3*y(k+2) + b4*y(k+3);
    if mod(k,2)==1, 
        plot(X,Y,'r-','LineWidth', 3); 
    else
        plot(X,Y,'k-','LineWidth', 3); 
    end
end
