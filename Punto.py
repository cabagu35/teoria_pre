class Punto:
    def __init__(self, x, y):
        """
        :param x: float
            coordenada x del punto
        :param y: float
            coordenada y del punto

        >>> p = Punto(1.0, 1.0)
        """
        self.__x = x #encapsulada
        self.y = y #no encapsulada

    def x(self):
        """
        >>> p = Punto(1.0, 2.0)
        >>> print(p.x())
        1.0
        """
        return self.__x

    def distancia(self, otro):
        """
        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(3.0, 2.0)
        >>> Q.distancia(P)
        2.0
        """
        return ((self.__x-otro.__x)**2+(self.y-otro.y)**2)**0.5

    def cuadrante(self):
        """
        Para x = 0 cae en los cuadrantes 1 o 2
        Para y = 0 cae en los cuadrantes 3 o 4
        >>> P = Punto(1.0, 2.0)
        >>> P.cuadrante()
        'Cuadrante 1'
        """
        if self.__x >= 0:
            if self.y >= 0:
                return 'Cuadrante 1'
            return 'Cuadrante 4'
        if self.y >= 0:
            return 'Cuadrante 2'
        return 'Cuadrante 3'




if __name__ == '__main__':
    import doctest

    print(doctest.testmod(verbose=True))