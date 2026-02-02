from turtle import *


#we want to paint a house

# draw a square
speed(26)
shape('turtle')


begin_fill()
width(7)
color('blue')
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color('orange')
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


left(30)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

left(90)
forward(60)

right(180)
forward(30)

right(90)
forward(60)

penup()
goto(200, 200)
pendown()


forward(60)
right(90)

forward(60)
right(90)


forward(60)
right(90)

forward(60)

right(180)
forward(30)

left(90)
forward(60)

bgcolor("green")





exitonclick()
