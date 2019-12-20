from turtle import *

ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)



startingPoint = -400
speed = 4

def convertAvanceeTortueParRaportALEcran(avance):
    screen = Screen()
    withTotal = screen.canvwidth
    return avance/2 - withTotal/2

def newTurtleQuiDoisPasSAppelerTurtle(color, height):
    newTurtle = Turtle()
    newTurtle.up()
    newTurtle.shape('turtle')
    newTurtle.color(color)
    newTurtle.speed(speed)
    newTurtle.goto(startingPoint, height)
    newTurtle.down()
    return newTurtle



turtle1 = newTurtleQuiDoisPasSAppelerTurtle("Orange", 100)
turtle2 = newTurtleQuiDoisPasSAppelerTurtle("Deep Sky Blue", 50)
turtle3 = newTurtleQuiDoisPasSAppelerTurtle("Red", 0)
turtle4 = newTurtleQuiDoisPasSAppelerTurtle("Dark Slate Gray", -50)
turtle5 = newTurtleQuiDoisPasSAppelerTurtle("Purple", -100)

for x in range(1,100):
    turtle1.goto(convertAvanceeTortueParRaportALEcran(x*3), 100)

input()