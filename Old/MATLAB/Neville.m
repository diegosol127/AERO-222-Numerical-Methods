chiudi;

val = 27.5;
P = zeros(5,5);
X = [32.0, 22.2, 41.6, 10.1, 50.5];
P(:,1) = [0.52992; 0.37784; 0.66393; 0.17537; 0.63608];
figure; x = linspace(10, 60, 100);
plot(X,P(:,1),'k*', x, sind(x),'r-'); grid on;
for j = 1:4
    for i = 1:5-j
        P(i,j+1)=((val-X(i))*P(i+1,j)+(X(i+j)-val)*P(i,j))/(X(i+j)-X(i));
     end
end
P,

format long,
P(1,2:end)-P(1,1:end-1),