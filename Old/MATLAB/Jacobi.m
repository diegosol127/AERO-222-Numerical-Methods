function x = Jacobi(A, b, x0, niter)

%% Jacobi

D = diag(diag(A));
O = A - D;
bp = D\b(:);
M = D\O;

x = x0;
for k = 1:niter
    x = bp - M*x;
end

end
