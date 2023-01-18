function [H, CN] = Hilbert(n)

H = ones(n);
for c = 1:n
    for r = 1:n
        H(r,c) = 1/(c + r - 1);
    end
end
CN = cond(H);
end