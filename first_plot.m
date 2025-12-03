clear;
clc;

grade	=	linspace(-10,10,60);
[xx,yy]	=	meshgrid(grade);
zz	=	cos(sqrt(xx.^2	+	yy.^2))	.*	sqrt(xx.^2	+	yy.^2);
contourf(xx,yy,zz)

