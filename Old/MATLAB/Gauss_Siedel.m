function x = Gauss_Siedel(A, b, x0, niter)

%% Gauss-Siedel

n = length(b);
D = diag(diag(A));
O = A - D;
bp = D\b(:);
M = D\O;

x = x0;
for k = 1:niter
    for j = 1:n
        x(j) = bp(j) - M(j,:)*x;
    end
end

end
