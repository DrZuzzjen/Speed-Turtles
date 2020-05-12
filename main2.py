import turtle
import random

class Circuito():
    corredores = []
    __posStartY =(-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, ancho, alto):
        self.__screen = turtle.Screen()  
        self.__screen.setup(ancho, alto)
        self.__screen.bgcolor('black')
        self.__startLine = -ancho/2 +20
        self.__finishLine = ancho/2 -20
        
        self.__creadorTortugas()
        
    def __creadorTortugas(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga {} ha ganado".format(tortuga.color()[0]))
                    break
        
            
if __name__ == '__main__':
    circuito = Circuito(640,480)
    circuito.competir()