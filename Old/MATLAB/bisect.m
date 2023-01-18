function xsol = bisect(f, a, b, ItMax, eps_step, eps_abs)
% Check that that neither end-point is a xsol
% and if f(a) and f(b) have the same sign, throw an exception.

if ( f(a) == 0 )
    xsol = a;
    return
elseif ( f(b) == 0 )
    xsol = b;
    return
elseif ( f(a) * f(b) > 0 )
    error('f(a) and f(b) do not have opposite signs');
end

% We will iterate ItMax times and if a xsol was not
% found after ItMax iterations, an exception will be thrown.

for iter = 1:ItMax
    % Find the mid-point
    c = (a + b)/2;
    
    % Check if we found a xsol or whether or not
    % we should continue with:
    %          [a, c] if f(a) and f(c) have opposite signs, or
    %          [c, b] if f(c) and f(b) have opposite signs.
    
    if ( f(c) == 0 )
        xsol = c;
        return
    elseif ( f(c)*f(a) < 0 )
        b = c;
    else
        a = c;
    end
    
    % If |b - a| < eps_step, check whether or not
    %       |f(a)| < |f(b)| and |f(a)| < eps_abs and return 'a', or
    %       |f(b)| < eps_abs and return 'b'.
    
    if ( abs(b - a) < eps_step )
        if ( abs( f(a) ) < abs( f(b) ) && abs( f(a) ) < eps_abs )
            xsol = a;
            return
        elseif ( abs( f(b) ) < eps_abs )
            xsol = b;
            return
        end
    end
end
error('the method did not converge');
end