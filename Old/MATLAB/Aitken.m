clear all; close all; clc;

% Aitken example

% Fixed pont function
g = @(x) (x + 2./x)/2;

% Initial value
x0 = 1;

% 10 digit accuracy is desired
tolerance = 10^-10;

% Don't want to divide by a number smaller than this
epsilon = 10^-16;
 
% Don't allow the iterations to continue indefinitely
maxIterations = 20;

% Were we able to find the solution to the desired tolerance? not yet.
FoundSolution = false;
 
for i = 1:maxIterations 
    x1 = g(x0);
    x2 = g(x1);
    den = x2 - 2*x1 + x0; 
    if(abs(den) < epsilon), disp('Denominator too small'); break; end
    x3 = x0 - (x1 - x0)^2/den;
%    x3 = x2 - (x2 - x1)^2/den;
    % If the result is within tolerance
    disp(['Iteration ' num2str(i) ': value = ' num2str(x3)]);
    if(abs(x3 - x2) < tolerance)
        disp(['Solution found: x-g(x) = ' num2str(x3-g(x3))]);
        FoundSolution = true; break
    end
    x0 = x3;
end
 
% If we weren't able to find a solution to within the desired tolerance
if(FoundSolution == false)
    disp(['Warning: Not able to find solution to within the desired tolerance of ' num2str(tolerance)]);
    disp(['The last computed extrapolate was ' num2str(x3)]);
end