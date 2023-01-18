function [x, k] = gauss_seidel(A, b, x0, xtrue, eps)
    n = length(A);
    x = x0;
    k = 0;
    while norm(x - xtrue) > eps
        for i = 1:n
            x(i) = (1/A(i, i))*(b(i) - A(i, 1:n)*x + A(i, i)*x(i));
        end
        k = k + 1;
    end    
end