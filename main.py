import turtle, os, colorgram, random
os.system("clear")

colors = []
for color in colorgram.extract('BadassUraraka.jpeg', 20):
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

window = turtle.Screen()
window.screensize(600, 525)
window.colormode(255)


tom = turtle.Turtle()
tom.hideturtle()
tom.speed(10)
tom.penup()

for y in range(-310, 310, 66):
    for x in range(-330, 390, 66):
        tom.goto(x, y)
        tom.dot(20, random.choice(colors))


window.exitonclick()
