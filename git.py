import turtle


screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")


heart = turtle.Turtle()
heart.speed(2)
heart.color("red")
heart.fillcolor("red")
heart.begin_fill()


heart.left(140)
heart.forward(180)
heart.circle(-90, 200)

# Draw the right side of the heart
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)

heart.end_fill()

heart.penup()
heart.goto(-100, -50)
heart.color("black")
heart.write(" i love india", font=("Arial", 20, "bold"))

heart.hideturtle()

screen.mainloop()
