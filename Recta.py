from Punto_1 import *

class Recta:
    def __init__(self, P1, P2=Punto(0.0, 0.0)):
        """
        PARAMETROS:
        ___________
        P1: Punto
            Punto 1 de la recta
        P2: Punto
            Punto 2 de la recta, por defecto es el origen

        >>> R = Recta(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> print(R)
        (1.0,1.0)-(2.0,2.0)
        """
        self.P1 = P1
        self.P2 = P2

    def __str__(self):
        """
        Metodo para imprimir la recta en formato (x1, y1)-(x2, y2)

        RETURN:
        _______
        str
            Representacion de la recta en formato (x1, y1)-(x2, y2)

        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(4.0, 2.0)
        >>> R = Recta(P, Q)
        >>> print(R)
        (1.0,2.0)-(4.0,2.0)

        :return:
        """
        return str(self.P1) + '-' + str(self.P2)

    def m(self):
        """
        Metodo para calcular la pendiente de una recta

        RETURN:
        _______
        float
            Pendiente de la recta

        >>> r = Recta(Punto(1, 1), Punto(2, 2))
        >>> r.m()
        1.0
        """
        if self.P1.x == self.P2.x:
            return float("inf")
        return (self.P1.y - self.P2.y) / (self.P1.x - self.P2.x)

    def b(self):
        """
        Metodo para calcular el intercepto de una recta

        RETURN:
        _______
        float
            Intercepto de la recta

        >>> R = Recta(Punto(1.0, 1.0))
        >>> print(R)
        (1.0,1.0)-(0.0,0.0)
        >>> R.b()
        0.0
        >>> r = Recta(Punto(0, 0), Punto(0, 1))
        >>> r.b()
        nan
        """
        return self.P1.y - self.m() * self.P1.x

    def perpendicular(self, otro):
        """
        Metodo para calcular la recta perpendicular a la recta que pasa por un punto

        PARAMETROS:
        ___________
        Punto: Punto
            Punto por el que pasa la recta perpendicular
        RETURN:
        _______
        Recta
            Recta perpendicular a la recta que pasa por el punto

        >>> P1 = Punto(1.0, 1.0)
        >>> P2 = Punto(1.0, -1.0)
        >>> R1 = Recta(P1)
        >>> print(R1.perpendicular(P2))
        (1.0,-1.0)-(0.0,0.0)

        """
        if self.m() == 0:
            return Recta(otro, Punto(0.0, otro.y))
        if self.m() == float("inf"):
            return Recta(otro, Punto(otro.x, 0.0))
        mperp = -1/self.m()
        bperp = otro.y - mperp * otro.x
        return Recta(otro, Punto(0.0, bperp))

    def interseccion(self, otra):
        """
        Metodo para calcular el punto de interseccion de dos rectas

        PARAMETROS:
        ___________
        otra: Recta
            Recta con la que se quiere calcular la interseccion
        RETURN:
        _______
        Punto
            Punto de interseccion de las dos rectas

        >>> R = Recta(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> S = Recta(Punto(1.0, 2.0), Punto(2.0, 1.0))
        >>> print(R.interseccion(S))
        (1.5,1.5)
        """
        if self.m() == otra.m():
            return None
        x = (self.b() - otra.b()) / (otra.m() - self.m())
        y = self.m() * x + self.b()
        return Punto(x, y)

    def distancia(self, P):
        """
        Metodo para calcular la distancia entre un punto y una recta
        PARAMETROS:
        ___________
        P: Punto
            Punto del que se quiere calcular la distancia
        RETURN:
        _______
        float
            Distancia entre el punto y la recta

        >>> R = Recta(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> Punto = Punto(1.0, 2.0)
        >>> R.distancia(Punto)
        0.7071067811865476
        """
        rectaperp = self.perpendicular(P)
        puntointers = self.interseccion(rectaperp)
        dist = P.distancia(puntointers)
        return dist

if __name__ == '__main__':
    import doctest

    print(doctest.testmod(verbose=True))
