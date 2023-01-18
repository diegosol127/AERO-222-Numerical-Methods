%% Error of interpolation
chiudi;
N = 1000;
x = linspace(1, 8, N);
f = exp(-x/2);

np1 = 5;
X = [1.1, 2.0, 3.5, 5.0, 7.1];
F = exp(-X/2);
P = polyval(polyfit(X, F, 4), x);

subplot(2,1,1), plot(x, f, 'k-', x, P, 'r-'); grid on;  
ylabel('f = exp(-x/2)'); hold on;
subplot(2,1,1), plot(X, F, 'k*'); xlabel('x');
 
E = ones(1, N);
for k = 1:np1
    E = E.*(x - X(k));
end
E = (-1)^np1/factorial(np1)*E.*exp(-x/2);
subplot(2,1,2), plot(x, E, 'k-', x, f-P, 'r-'); xlabel('x'); ylabel('Error'); grid on;
