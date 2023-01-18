
%% Parameters

clear; close all; clc;

% tol = 1e-12;                         
% options = odeset('RelTol', tol, 'AbsTol', tol*1e-3);
options = odeset();

% Set up the system
Y0 = [0 1 1]';
t0 = 0; t1 = 1;
tSpan = [t0 t1];

[t,Y] = ode45(@DiffEq, tSpan, Y0, options);
y   = Y(:,1);
yp  = Y(:,2);
ypp = Y(:,3);

figure()
plot(t, y); grid on; hold on;
plot(t, yp);
plot(t, ypp);
legend('y', 'y`', 'y``');
xlabel t
ylabel State

%% manually setting the time

tVector = linspace(t0, t1, 5);
[t,Y] = ode45(@DiffEq, tVector, Y0, options);
y   = Y(:,1);
yp  = Y(:,2);
ypp = Y(:,3);

figure()
plot(t, y); grid on; hold on;
plot(t, yp);
plot(t, ypp);
legend('y', 'y`', 'y``');
xlabel t
ylabel S5tate




