function [L, U] = LUX (A)

%% Performs LU decomposition

[n, col] = size(A);
if n ~= col, return; end
L = eye(n);

%% Scaled partial pivoting
% for row = 1:n
%     [~, I] = max(abs(A(row,1:n)));
%     disp(['Scaled partial pivoting in row ' num2str(row)]);
%     A(row,:) = A(row,:)/A(row,I);
% end

%% Part Ib: Swapping and partial pivoting
for col = 1:n-1
    [~, I] = max(abs(A(col:n, col)));
    I = I + col - 1;
    if I ~= col
        [A(col, :), A(I, :)] = swap(A(col, :), A(I, :)),
        disp(['Swapping row ' num2str(I) ' and ' num2str(col)]);
    end
    for row = col+1:n
        L(row, col) = A(row,col)/A(col,col);
        A(row,:) = A(row,:) - A(col,:)*A(row,col)/A(col,col),
        disp(['Reducing element (' num2str(row) ',' num2str(col) ')']);
    end
end
U = A;

end
