# Trabajo clonado y adaptado de: https://www.geeksforgeeks.org/create-a-simple-animation-using-turtle-in-python/
# Adaptacion: Daniel Esteban Valencia (Es decir, el dueño de este repositorio)
# id: 224159X
# required modules
from turtle import * 
from random import randint

	
# Forma base de la tortuga
speed(0)
penup()
goto(-140, 140)

# Pita de carrera
for step in range(16):
	write(step, align ='center')
	right(90)
	
	for num in range(9):
		penup()
		forward(10)
		pendown()
		forward(10)
		
	penup()
	backward(180)
	left(90)
	forward(20)

# ----------------------------------------------------------------------------
# Detalles de Primera tortuga 
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# Primera tortuga entra a la carrera
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# Giro de 360 grados
for turn in range(10):
	player_1.right(36)

# ----------------------------------------------------------------------------

# Detalles de la segunda tortuga
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# Segunda tortuga entra a la carrera
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# Giro de 360 grados
for turn in range(72):
	player_2.left(5)

# ----------------------------------------------------------------------------

# Detalles de la tercera tortuga
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# Tercera tortuga entra a la carrera
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# Giro de 360 grados
for turn in range(60):
	player_3.right(6)

# ---------------------------------------------------------------------------

# Detalles de la cuarta tortuga
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# Cuarta tortuga entra a la carrera
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# Giro de 360 grados
for turn in range(30):
	player_4.left(12)

# ---------------------------------------------------------------------------

# detalles de la quinta tortuga
player_5 = Turtle()
player_5.shape('turtle')
player_5.color('pink')

# La quinta tortuga entra a la carrera
player_5.penup()
player_5.goto(-160, -20)
player_5.pendown()

# Giro de 360 grados
for turn in range(60):
	player_5.right(6)

# --------------------------------------------------------------------------------------------

# Las tortugas Se mueven a diferentes velocidades
for turn in range(100):
	player_1.forward(randint(1, 5))
	player_2.forward(randint(1, 5))
	player_3.forward(randint(1, 5))
	player_4.forward(randint(1, 5))
	player_5.forward(randint(1, 5)) # Yo apostaria mas por esta tortuga jeje

#-------------------------------------------------------------------------------------------
# Crear una lista para almacenar todas las tortugas
tortugas = [player_1, player_2, player_3, player_4, player_5]

# Inicializar la tortuga ganadora y la distancia máxima
ganadora = None
distancia_maxima = 100

# Iterar sobre todas las tortugas
for i, tortuga in enumerate(tortugas):
    # Obtener la distancia recorrida por la tortuga actual
    distancia = tortuga.position()[0]  # Solo nos interesa la coordenada x

    # Si la tortuga actual ha recorrido más distancia que la ganadora actual
    if distancia > distancia_maxima:
        # Actualizar la ganadora y la distancia máxima
        ganadora = i + 1  
        distancia_maxima = distancia

# Imprimir la tortuga ganadora
print("La tortuga", ganadora, "gana")
