close all; clear all; clc;

%% True solution
XT = linspace(0, 0.6, 100);
YT = 2 - 3*exp(-XT) - 2*XT;
y0 = YT(1);

%% Simulation with step = 0.1 between 0 and 0.6
N = 7;
X = linspace(0, 0.6, N);

%% Taylor-series Method
y1 = - y0;
y2 = - 2 - y1;
y3 = - y2;
y4 = - y3;
h = X;
yt = y0 + y1*h + y2/2*h.^2 + y3/3*h.^3 + y4/12*h.^4;

%% Euler Method
h = X(2) - X(1);
ye = y0*ones(1, N);
for k = 2:N
    yp = -2*X(k-1) - ye(k-1);
    ye(k) = ye(k-1) + h*yp;
end

%% Improved Euler Method
yi = y0*ones(1, N);
for k = 2:N
    yp =-2*X(k-1) - yi(k-1);
    yie = yi(k-1) + h*yp;
    ype =-2*X(k) - yie;
    yi(k) = yi(k-1) + h*yp + (ype - yp)/2*h;
end

plot(XT,YT,'k-',X,yt,'r-',X,ye,'b-',X,yi,'g-'); grid on; hold on;
legend('True','Taylor', 'Euler','Improved'); xlabel('x'); ylabel('y(x)');
plot(X,yt,'r*',X,ye,'b*',X,yi,'g*','MarkerSize',12);
