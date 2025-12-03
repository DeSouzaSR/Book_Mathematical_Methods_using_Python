clear
clc

x = linspace(0, 10, 1000);
y1 = sin(x);
y2 = sin(x) .* sin(7*x);

plot(x, y1, '--',x ,y2);
legend("Funções moduladora", "Função modulada");

