function [T, Y] = ImprovedEulerVector(fnc, TRange, Y0, N, AddPar)

%% Improved Euler for first-order ODE
%
t0 = TRange(1);
tf = TRange(2);
h = (tf - t0)/N;               % stepsize h

T = zeros(N+1, 1); 
Y = zeros(N+1, length(Y0));

t = t0; y = Y0;                % initial point
T(1) = t; 
Y(1,:) = y';
for i = 1:N
%    whos t y,
    s1 = fnc(t, y, AddPar);    % evaluate direction field at current point
    yE = y + s1*h;             % find Euler value yE
    s2 = fnc(t+h,yE, AddPar);  % evaluate direction field at Euler point
    y = y + (s1+s2)/2*h;       % use mean (s1+s2)/2 to find new y
    t = t + h;
    T(i+1) = t; 
    Y(i+1,:) = y';              % store y(1),y(2) in row of array Y
end
end
