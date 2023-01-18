function x = GaussElimination(A, b)

%% Performs Gauss elimination with back substitution using the augmented matrix

n = length(b);
disp('Augmented matrix');
Ag = [A, b],

%% Part Ia. Scaled partial pivoting
for row = 1:n
    [~, I] = max(abs(Ag(row,1:n)));
    disp(['Scaled partial pivoting in row ' num2str(row)]);
    Ag(row,:) = Ag(row,:)/A(row,I),
end

%% Part Ib: Swapping and partial pivoting
for col = 1:n-1
    [~, I] = max(abs(Ag(col:n, col)));
    I = I + col - 1;
    if I ~= col
        [Ag(col, :), Ag(I, :)] = swap(Ag(col, :), Ag(I, :));
        disp(['Swapping row ' num2str(I) ' and ' num2str(col)]);
        Ag,
    end
    for row = col+1:n
        Ag(row,:) = Ag(row,:) - Ag(col,:)*Ag(row,col)/Ag(col,col);
        disp(['Reducing element (' num2str(row) ',' num2str(col) ')']);
        Ag,
    end
end

%% Part II: Back substitution
x = zeros(n, 1);
x(n) = Ag(n,n+1)/Ag(n,n);
for i = n-1:-1:1
    s = Ag(i,n+1);
    for j = i+1:n
        s = s - Ag(i,j)*x(j);
    end
    x(i) = s/Ag(i,i);
end

end
