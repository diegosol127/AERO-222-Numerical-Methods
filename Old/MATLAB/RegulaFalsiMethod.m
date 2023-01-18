function xsol = RegulaFalsiMethod (f, x1, x2, ItMax, ConvTol)

%% Implement the regula falsi method

fx1 = f(x1);
fx2 = f(x2);
c = x2 - ((f(x2)*(x2 - x1))/(f(x2) - f(x1)));
fc = f(c);
it = 0;
if fx1*fx2 < 0
    while abs(fc) > ConvTol
        if fc < 0
            x1 = c;
            fx1 = f(x1);
            c = x1 - (fx1*(x1 - x2)/(fx1 - fx2));
            fc = f(c);
        else
            x2 = c;
            fx2 = f(x2);
            c = x2 - (fx2*(x2 - x1)/(fx2 - fx1));
            fc = f(c);
        end
        it = it + 1;
        if it > ItMax
            xsol = [];
            disp(['Number of iterations exceeds ' num2str(ItMax)]);
            return
        end
    end
    xsol = c;
else
    disp(['--->      f(' num2str(x1) ') = ' num2str(fx1)]);
    disp(['--->      f(' num2str(x2) ') = ' num2str(fx2)]);
    error('From RegulaFalsiMethod: root must be bracket.');
end

end
