function	[raiz_1,	raiz_2]	=	quad(val_a,	val_b,	val_c)
  %{
    [raiz_1,	raiz_2]	=	quad(val_a,	val_b,	val_c)

    QUAD	encontra	as	raízes	(ou	zeros)	X1	(raiz_1)	e	X2	(raiz_2)
    da	equação	quadrática	A*X^2	+	B*X	+	C	=	0	pela	fórmula	de
    Bhaskara.
  %}
  delta	=	val_b^2	-	4*val_a*val_c;
  raiz_1	=	(-val_b	+	sqrt(delta))./(2*val_a);
  raiz_2	=	(-val_b	-	sqrt(delta))./(2*val_a);
end
