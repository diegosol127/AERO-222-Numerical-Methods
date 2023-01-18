function dx = ExpConvergence(dx1, n1, dx2, n2, n3)

%% Exponential convergence estimator. Daniele Mortari - 6-10-2020

if dx1*dx2 > 0, segno = 1; else, segno =-1; end

b = (log(dx1) - log(dx2))/(n2 - n1);
if n1 < n2
    dx = segno*dx1*exp(b*(n1 - n3));
else
    dx = segno*dx2*exp(b*(n2 - n3));
end

end