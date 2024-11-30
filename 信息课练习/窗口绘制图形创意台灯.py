import turtle

turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(100,0)
turtle.goto(50,50)
turtle.goto(0,0)
turtle.end_fill()

turtle.penup()
turtle.goto(50,-20)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.hideturtle()
