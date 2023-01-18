clear; close all; clc;

%% Kepler equation convergence range
M = deg2rad(25);
e = 0.3;

N = 100;
E = linspace(-pi, pi, N);
y = E - (M - E + e*sin(E))./(e*cos(E) - 1);
subplot(211), plot(E, E, 'k-', E, y, 'r-','LineWidth', 3); grid on;
xlabel('Eccentric anomaly ($E$)'); ylabel('$g(E)$'); 
title(['Mean anomaly = ' num2str(cw*M) ' deg.; Eccentricity = ' num2str(e)]);

gp = abs(e*sin(E).*(M - E + e*sin(E)))./(e*cos(E)-1).^2;
subplot(212), plot(E, gp, 'r-','LineWidth', 3); grid on;
xlabel('Eccentric anomaly ($E$)'); ylabel('$| g''(E) |$');
