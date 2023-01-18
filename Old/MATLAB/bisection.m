function [x0, err] = bisection(xn,xp)
maxit = 100;
tol = 1.0e-6;
err = 100.0;
icount = 0;
fn = funkeval(xn);
fp = funkeval(xp);
while (err > tol && icount <= maxit)
 icount = icount + 1;
 xmid = (xn + xp)/2;
 fmid = funkeval(xmid);
 if (fmid > 0)
 fp = fmid;
 xp = xmid;
 else
 fn = fmid;
 xn = xmid;
 end
 err = abs((xp - xn)/xp);
 fprintf(1,'icount = %i xn = %e xp = %e fn = %e fp = %e err = %e \n',icount, xn, xp, fn, fp, err);
end
%
x0 = xmid;
if (icount >= maxit)
 % you ran out of iterations
 fprintf(1,'Sorry. You did not converge in %i iterations.\n',maxit);
 fprintf(1,'The final value of x was %e \n', x0);
 fprintf(1,'Maybe you should try a better method because Bisection Method is slow as a dog. \n');
end

function f = funkeval(x)
f = x + log(x);