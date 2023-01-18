function [P,L,U] = PLU(A)

% This gives the P*L*U decomposition of A

n = size(A, 1);

%% augmented matrix with the permutation matrix
AP = [A, eye(n)];

for k = 1:n-1
    %% Partial pivoting
    [akx, kx] = max(abs(AP(k:n,k)));
    if akx < eps
        error('Singular matrix and No PLU decomposition')
    end
    mx = k+kx-1;
    [AP(k,:), AP(mx,:)] = swap(AP(k,:), AP(mx,:));
    %% LU decomposition
    for m = k+1:n
        AP(m,k) = AP(m,k)/AP(k,k);
        AP(m,k+1:n) = AP(m,k + 1:n) - AP(m,k)*AP(k,k + 1:n);
    end
end

%% Permutation matrix
P = round(AP(:,n+1:2*n))';

%% Storing L and U matrices
L = eye(n); 
U = zeros(n);
for m = 1:n
    for n = 1:n
        if m <= n 
            U(m,m) = AP(m,m);
        else
            L(m,n) = AP(m,n); 
        end
    end
end

end