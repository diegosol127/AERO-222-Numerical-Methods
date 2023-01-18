clear; close all; clc;

%% Provides the coefficients of the numerical deg derivative 
%% using the points from Imin to Imax 
%
%% Example: to obtain f_i" usinf[f_{i-1}, f_i, f_{i+1}, f_{i+1}, f_{i+3}]
%%           use: Imain = -1;  Imax = 3,  and  deg = 2;
%
%% Daniele Mortari   -   Texas A&M University   -   20 July 2022
%
Imin =-3;
Imax = 3;
deg = 1;

I = Imin:Imax;
n = length(I);
fct = 1./factorial(1:n-1);

M = zeros(n-1);
r = 0;
for k = 1:n
    if I(k) ~= 0
        r = r + 1;
        M(r,:) = fct.*(I(k).^(1:n-1));
    end
end
b = zeros(n-1,1); b(deg) = 1;
C = (M')\b;

r = 0;
Coef = zeros(1, n);
for k = 1:n
    if I(k) ~= 0
        r = r + 1;
        Coef(k) = C(r);
    else
        Coef(k) =-sum(C);
    end
end
[N,D] = rat(Coef),
precision = n - deg,

