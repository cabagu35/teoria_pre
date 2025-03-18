from Recta import *

class Segmento(Recta):
    def longitud(self):
        """
        Metodo para calcular la longitud de un segmento

        RETURN:
        _______
        float
            Longitud del segmento

        >>> s = Segmento(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> print(s)
        (1.0,1.0)-(2.0,2.0)
        >>> s.longitud()
        1.4142135623730951
        """
        return self.P1.distancia(self.P2)

    def pasa(self, P):
        """
        Metodo para determinar si un punto pertenece a un segmento

        PARAMETROS:
        ___________
        P: Punto
            Punto a evaluar
        RETURN:
        _______
        bool
            True si el punto pertenece al segmento, False en caso contrario

        >>> s = Segmento(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> s.pasa(Punto(1.5, 1.5))
        True
        >>> s.pasa(Punto(1.5, 1.6))
        False
        """
        return self.P1.distancia(P) + self.P2.distancia(P) == self.longitud()

    def interseccion(self, otra):
        """
        Especialización del metodo para calcular el punto de interseccion de dos segmentos

        PARAMETROS:
        ___________
        otra: Segmento
            Segmento con el que se quiere calcular la interseccion
        RETURN:
        _______
        Punto
            Punto de interseccion de los dos segmentos

        >>> s = Segmento(Punto(1.0, 1.0), Punto(2.0, 2.0))
        >>> t = Segmento(Punto(1.0, 2.0), Punto(2.0, 1.0))
        >>> print(s.interseccion(t))
        (1.5,1.5)
        """
        p = Recta.interseccion(self, otra)
        if p is None or not (self.pasa(p) and otra.pasa(p)):
            return None
        return p

    def __eq__(self, otro):
        """
        Sobrecarga del operador == para segmentos

        PARAMETROS:
        ___________
        otro: Segmento
            Segmento con el que se quiere comparar
        RETURN:
        _______
        bool
            True si los segmentos son iguales, False en caso contrario

        >>> P1 = Punto(1.0, 1.0)
        >>> P2 = Punto(2.0, 2.0)
        >>> S1 = Segmento(P1, P2)
        >>> S2 = Segmento(P1, P2)
        >>> S3 = Segmento(Punto(1.0, 1.0), Punto(3.0, 3.0))
        >>> S1 == S2
        True
        >>> S1 == S3
        False
        """
        return (self.P1 == otro.P1 and self.P2 == otro.P2) or (self.P1 == otro.P2 and self.P2 == otro.P1)

    def medio(self):
        """
        Metodo para calcular el punto medio de un segmento

        RETURN:
        _______
        Punto
            Punto medio del segmento

        >>> P = Punto(1.0, 1.0)
        >>> Q = Punto(3.0, 3.0)
        >>> S = Segmento(P, Q)
        >>> print(S.medio())
        (2.0,2.0)
        """
        x_medio = (self.P1.x + self.P2.x) / 2
        y_medio = (self.P1.y + self.P2.y) / 2
        return Punto(x_medio, y_medio)

    def distancia(self, P):
        """
        Metodo para calcular la distancia entre un punto y un segmento
        ...
        """
        rectaperp = self.perpendicular(P)  # Crear la recta perpendicular desde el punto P
        puntointers = self.interseccion(rectaperp)  # Encontrar el punto de intersección
        if puntointers is None:
            # Si no hay intersección, se puede calcular la distancia a los extremos
            return min(P.distancia(self.P1), P.distancia(self.P2))
        # Utilizar el método distancia de Punto para calcular la distancia al punto de intersección
        return P.distancia(puntointers)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=True))
