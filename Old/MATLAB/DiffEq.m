function Yp = DiffEq(t,Y)

A = [0 1 0; 0 0 1; 2 1 -2];
Yp = A*Y;