import turtle

class Circuito():
    corredores: []
    
    def __init__(self, ancho, alto):
        self.__screen = turtle.Screen()  
        self.__screen.setup(ancho, alto)
        self.__screen.bgcolor('lightgray')
        
if __name__ == "__main__":
    circuito = Circuito(640, 480)
        