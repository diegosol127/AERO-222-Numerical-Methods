function xsol = SecantMethod(f, a, b, IterMax, ConvTol)
% USAGE: xsol = SecantMethod(f, a, b, IterMax, ConvTol)
%
% Implements the secant method
%
% Input:
%        a = initial guess for the root of f
%        b = another initial guess for the root of f
%  IterMax = maximum number of iterations
%  ConvTol = the tolerance/accuracy we desire
%
% Output:
%     xsol = the approximation to the root of f
%

Iter = 0;
fa = f(a); 
fb = f(b);
fmax = 1000*abs(max([fa, fb]));
c = b - (a - b)/(fa - fb);
fc = f(c);
while abs(fc) > ConvTol
        disp(['     (a): abs(f(' num2str(a) ') = ' num2str(fa)]);
        disp(['     (b): abs(f(' num2str(b) ') = ' num2str(fb)]);
        disp(['---> (c): abs(f(' num2str(c) ') = ' num2str(fc)]);
    a = b;
    b = c;
    fa = fb;
    fb = fc;
    c = b - (a - b)/(fa - fb);
    fc = f(c);
    if abs(fc) > fmax
        disp( '---> Secant is diverging');
        disp(['     (a): abs(f(' num2str(a) ') = ' num2str(fa)]);
        disp(['     (b): abs(f(' num2str(b) ') = ' num2str(fb)]);
        disp(['---> (c): abs(f(' num2str(c) ') = ' num2str(fc)]);
        xsol = [];
        return
    end 
    Iter = Iter + 1;
    if Iter >= IterMax, 
        xsol = [];
        disp(['Number of iterations exceeds ' num2str(IterMax)]);
        return
    end
end
xsol = c;

end