import turtle

turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(50,0)
turtle.goto(50,100)
turtle.goto(0,100)
turtle.goto(0,0)
turtle.end_fill()

turtle.penup()
turtle.goto(10,20)
turtle.pendown()

turtle.fillcolor("white")
turtle.begin_fill()
turtle.goto(15,20)
turtle.goto(15,80)
turtle.goto(10,80)
turtle.goto(10,20)
turtle.end_fill()

turtle.hideturtle()
