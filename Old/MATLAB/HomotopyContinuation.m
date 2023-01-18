clear; close all; clc;

nimax = 100;
epsy = 1e-8;
f  =@(x) 2*x - 4 + sin(2*pi*x);
fd =@(x) 2 + 2*pi*cos(2*pi*x);
x0 = 0;
H  =@(t, x) f(x) + (t - 1)*f(x0);
Nx = 101; U = ones(1,Nx); x = linspace(-1/2,2.5,Nx);
Nt = 21; T = linspace(0,1,Nt); NIT = T; X = T;
plot3(x0,0,0,'r*'); hold on;
xk = x0;
for k = 1:Nt
    t = T(k);
    ni = 0;
    while 1
        ni = ni + 1; if ni > nimax, break, end
        xk = xk - H(t, xk)/fd(xk);
        if abs(H(t, xk)) < epsy, break, end
    end
    if ni > nimax
        disp(['Number of iterations > ' num2str(nimax)]);
        return,
    end
    disp(['t = ' num2str(t) '; Niter = ' num2str(ni) '; x = ' num2str(xk)]);
    X(k) = xk;
    NIT(k) = ni;
    plot3(t*U, x, H(t,x),'k.',t, xk, 0,'r*');
end
grid on;

p1 = [T(1), x(1), 0];
p2 = [T(Nt), x(1), 0];
p3 = [T(Nt), x(Nx), 0];
p4 = [T(1), x(Nx), 0]; 

TT = [p1(1) p2(1) p3(1) p4(1)];
XX = [p1(2) p2(2) p3(2) p4(2)];
HH = [p1(3) p2(3) p3(3) p4(3)];

fill3(TT, XX, HH, 1);
xlabel('$t$'); ylabel('$x$'); zlabel('$H(t, x)$'); % alpha(0.3)
 
figure;
plot(x, f(x),'k-',x0, f(x0),'r*'); grid on; 
xlabel('$x$'); ylabel('$f(x)$');