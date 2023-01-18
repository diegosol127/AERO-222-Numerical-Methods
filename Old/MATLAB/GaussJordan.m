function X = GaussJordan (A, B)

%% Perform Gauss-Jordan method

[n, m] = size(B);
M = [A, B];
disp('1) Initial matrix:')
M,

%% Part Ia. Scaled partial pivoting
for k = 1:n
    [~, I] = max(abs(M(k,1:n)));
    M(k,:) = M(k,:)/M(k,I);
end
disp('After the scaled partial pivoting ... ')
M,

%% Part Ib: Swapping and partial pivoting
for c = 1:n
    [~, I] = max(abs(M(c:n, c)));
    I = I + c - 1;
    if c ~= I
        disp(['Swapping row ' num2str(c) ' and row ' num2str(I)])
        [M(c, :), M(I, :)] = swap(M(c, :), M(I, :));
        M,
    end
    disp(['Reduce to 1 the element (' num2str(c) ',' num2str(c) ')'])
    M(c, :) = M(c, :)/M(c, c);
    M,
    for r = 1:n
        if r ~= c
            disp(['Making element (' num2str(r) ',' num2str(c) ') = 0'])
            M(r,:) = M(r,:) - M(c,:)*M(r,c)/M(c,c);
            M,
        end
    end
end

X = M(:, n+1:n+m);

end
