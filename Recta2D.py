from Punto import * #poniendo asterisco nos sirve para no tener que llamar la función Punto cada vez ej. Punto.Punto(1.0, 2.0)

class Recta:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2


    def __str__(self):
        """
        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(4.0, 2.0)
        >>> R = Recta(P, Q)
        >>> print(R)
        (1.0,2.0)-(4.0,2.0)
        """
        return str(self.P1) + '-' + str(self.P2)

    def perpendicular(self, Punto):
        pass

    def interseccion(self, Recta):
        pass


    def distancia(self, Punto): #No ponemos el parámetro recta porque es el self
        recta_perp = self.perpendicular(Punto)
        punto_inters = self.interseccion(recta_perp)
        dist = Punto.distance(punto_inters)
        return dist




if __name__ == '__main__':
    import doctest

    print(doctest.testmod(verbose=True))