import turtle

# Configuração da Tartaruga
t = turtle.Turtle()
t.speed(2)
t.color('red')
t.fillcolor('red')

# Desenha o coração com base a distancia a ser percorrida
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

# Esconde a tartaruga
t.hideturtle()

# Mantém a janela aberta
turtle.mainloop()
