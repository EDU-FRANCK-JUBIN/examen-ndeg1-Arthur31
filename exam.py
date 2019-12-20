import turtle 




# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("fond.gif")

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



# Declarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
turtle1 = newTurtleQuiDoisPasSAppelerTurtle("Orange", 100)
turtle2 = newTurtleQuiDoisPasSAppelerTurtle("Deep Sky Blue", 50)
turtle3 = newTurtleQuiDoisPasSAppelerTurtle("Red", 0)
turtle4 = newTurtleQuiDoisPasSAppelerTurtle("Dark Slate Gray", -50)
turtle5 = newTurtleQuiDoisPasSAppelerTurtle("Purple", -100)

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
# A IMPLEMENTER



# Comparer les rÃ©sultats de la course avec les pronostics des joueurs 
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 Ã  gagnÃ©", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()