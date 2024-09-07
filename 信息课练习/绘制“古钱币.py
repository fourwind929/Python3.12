import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.penup()
turtle.goto(-20,40)
turtle.pendown()

turtle.fillcolor("white")
turtle.begin_fill()
turtle.goto(20,40)
turtle.goto(20,80)
turtle.goto(-20,80)
turtle.goto(-20,40)
turtle.end_fill()

turtle.hideturtle()
