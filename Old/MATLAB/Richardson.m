ckear all; close all; clc;

tStart = 0;          %Starting time
tEnd = 5;            %Ending time
f =-y^2;            %The derivative of y, so y' = f(t, y(t)) = -y^2
                    % The solution to this ODE is y = 1/(1 + t)
y0 = 1;              %The initial position (i.e. y0 = y(tStart) = y(0) = 1)
tolerance = 10^(-11);  %10 digit accuracy is desired
 
maxRows = 20;                %Don't allow the iteration to continue indefinitely
initialH = tStart - tEnd;    %Pick an initial step size
haveWeFoundSolution = false; %Were we able to find the solution to the desired tolerance? not yet.
 
h = initialH;
 
%Create a 2D matrix of size maxRows by maxRows to hold the Richardson extrapolates
%Note that this will be a lower triangular matrix and that at most two rows are actually
% needed at any time in the compuation.
A = zeroMatrix(maxRows, maxRows);
 
%Compute the top left element of the matrix
A(1, 1) = Trapezoidal(f, tStart, tEnd, h, y0);
 
%Each row of the matrix requires one call to Trapezoidal
%This loops starts by filling the second row of the matrix, since the first row was computed above
for i = 1:maxRows-1 %Starting at i = 1, iterate at most maxRows - 1 times
    h = h/2;             %Half the previous value of h since this is the start of a new row
 
    %Call the Trapezoidal function with this new smaller step size
    A(i + 1, 1) = Trapezoidal(f, tStart, tEnd, h, y0);
 
    for j = 1:i         %Go across the row until the diagonal is reached
        %Use the last value computed (i.e. A(i + 1, j)) and the element from the
        % row above it (i.e. A(i, j)) to compute the next Richardson extrapolate
 
        A(i + 1, j + 1) = ((4^j).*A(i + 1, j) - A(i, j))/(4^j - 1);
    end
 
    %After leaving the above inner loop, the diagonal element of row i + 1 has been computed
    % This diagonal element is the last Richardson extrapolate to be computed  
    %The difference between this extrapolate and the last extrapolate of row i is a good
    % indication of the error
    if(absoluteValue(A(i + 1, i + 1) - A(i, i)) < tolerance)   %If the result is within tolerance
        print(['y(5) = ', num2str(A(i + 1, i + 1))]);                      %Display the result of the Richardson extrapolation
        haveWeFoundSolution = true;
        break                                                  %Done, so leave the loop
    end
end
 
if(haveWeFoundSolution == false)   %If we weren't able to find a solution to within the desired tolerance
    print(['Warning: Not able to find solution to within the desired tolerance of ', num2str(tolerance)]);
    print(['The last computed extrapolate was ', num2str(A(maxRows, maxRows))]);
end