clear all; close all; clc;

%% Ladder problem

N = 100;
c = linspace(0,180-123,N);
L = 9./sind(180-123-c)+7./sind(c);
semilogy(c,L,'LineWidth', 3), grid on;
xlabel('Angle c (deg)');
ylabel('Ladder length (feet)')