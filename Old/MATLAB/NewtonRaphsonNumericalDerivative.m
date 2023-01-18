function [x0, err] = NewtonRaphsonNumericalDerivative(x0)
%
% Newton-Raphson method with numerical approximations to the derivative.
%
maxit = 100;
tol = 1.0e-6;
err = 100.0;
icount = 0;
xold = x0;
while (err > tol && icount <= maxit)
    icount = icount + 1;
    f = funkeval(xold);
    h = min(0.01*xold, 0.01);
    df = dfunkeval(xold, h);
    xnew = xold - f/df;
    if (icount > 1)
        err = abs((xnew - xold)/xnew);
    end
    fprintf(1,'icount = %i xold = %e f = %e df = %e xnew = %e err = %e \n',icount, xold, f, df, xnew, err);
    %fprintf(1,'%i %e %e %e %e %e \n',icount, xold, f, df, xnew, err);
    xold = xnew;
end

x0 = xnew;
if (icount >= maxit)
    % you ran out of iterations
    fprintf(1,'Sorry. You did not converge in %i iterations.\n',maxit);
    fprintf(1,'The final value of x was %e \n', x0);
end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function f = funkeval(x)
f = x + log(x);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function df = dfunkeval(x,h)
fp = funkeval(x + h);
fn = funkeval(x - h);
df = (fp - fn)/(2*h);
end