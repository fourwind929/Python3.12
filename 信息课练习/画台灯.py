import turtle

turtle.setup(800,600)

turtle.speed(5)

turtle.penup()
turtle.goto(-300,100)
turtle.pendown()

turtle.fillcolor("green")
turtle.begin_fill()

turtle.goto(-100,100)
turtle.goto(-130,200)
turtle.goto(-270,200)
turtle.goto(-300,100)

turtle.end_fill()




turtle.penup()
turtle.goto(-220,100)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.goto(-220,-100)
turtle.goto(-180,-100)
turtle.goto(-180,100)
turtle.goto(-220,100)

turtle.end_fill()




turtle.penup()
turtle.goto(-235,-100)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()

turtle.goto(-165,-100)
turtle.goto(-165,-115)
turtle.goto(-235,-115)
turtle.goto(-235,-100)

turtle.end_fill()


turtle.hideturtle()

