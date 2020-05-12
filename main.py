import turtle

class Circuito():
    corredores: []
    __posStartY = (-30, -10, 10, 30)
    __colorT = ('red', 'blue', 'green', 'orange')
    
    
    def __init__(self, ancho, alto):
        self.__screen = turtle.Screen()  
        self.__screen.setup(ancho, alto)
        self.__screen.bgcolor('black')
        self.__startLine = -ancho/2 +20
        self.__finishLine = ancho/2 -20
        
        for i in range(4):
            tortuga = turtle.Turtle()
            tortuga.color(self.__colorT[i])
            tortuga.shape("turtle")
            tortuga.penup()
            tortuga.setpos(self.__startLine, self.__posStartY[i])
                
            self.corredores.append(tortuga)
            
            
   
   
   
   
   
   
   
if __name__ == "__main__":
    circuito = Circuito(640, 480)
        