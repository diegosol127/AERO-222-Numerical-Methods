function [x0, err] = NewtonRaphsonMethod(x0)
%
% Newton-Raphson method
%
maxit = 100;
tol = 1.0e-6;
err = 100.0;
icount = 0;
xold = x0;
while (err > tol && icount <= maxit)
    icount = icount + 1;
    f = funkeval(xold);
    df = dfunkeval(xold);
    xnew = xold - f/df;
    if (icount > 1)
        err = abs((xnew - xold)/xnew);
    end
    fprintf(1,'icount = %i xold = %e f = %e df = %e xnew = %e err = %e \n',icount, xold, f, df, xnew, err);
    xold = xnew;
end
%
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
function df = dfunkeval(x)
df = 1 + 1/x;
end
