function xsd = sigdig(x, N)

%% N = number of significal digits

E = round(log10(abs(x)));
xsd = sign(x)*(10^E)*round(abs(x)*10^(N-1-E))/10^(N-1);

end