class Punto:
    def __init__(self, x, y):
        """
        PARAMETROS:
        ___________
        x: float
            coordenada x del punto
        y: float
            coordenada y del punto

        >>> p = Punto(1.0, 2.0)
        >>> print(p.x)
        1.0
        >>> print(p.y)
        2.0
        >>> print(p)
        (1.0,2.0)
        """
        self.x = x
        self.y = y

    def distancia(self, otro):
        """
        Metodo para calcular la distancia entre dos puntos

        PARAMETROS:
        ___________
        otro: Punto
            Punto al que se quiere calcular la distancia
        RETURN:
        _______
        float
            Distancia entre los dos puntos

        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(3.0, 2.0)
        >>> Q.distancia(P) == 2.0
        True
        """
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2)**0.5

    def cuadrante(self):
        """
        Metodo para calcular el cuadrante en el que se encuentra el punto

        RETURN:
        _______
        int
            Cuadrante en el que se encuentra el punto
            Para x = 0 cae en los cuadrantes 1 o 2
            Para y = 0 cae en los cuadrantes 1 o 4

        >>> P = Punto(1.0, 2.0)
        >>> P.cuadrante()
        1
        """
        if self.x >= 0:
            if self.y >= 0:
                return 1
            return 4
        if self.y >= 0:
            return 2
        return 3

    def __str__(self):
        """
        Metodo para representar el punto como una cadena de caracteres

        RETURN:
        _______
        str
            Representacion del punto como una cadena de caracteres

        >>> P = Punto(1.0, 2.0)
        >>> print(P)
        (1.0,2.0)
        """
        return f'({self.x},{self.y})'

    def modulo(self):
        """
        Metodo para calcular el modulo del punto

        RETURN:
        _______
        float
            Modulo del punto

        >>> P = Punto(1, 1)
        >>> P.modulo()
        1.4142135623730951
        """
        return (self.x**2 + self.y**2)**0.5

    def medio(self, Q):
        """
        Metodo para calcular el punto medio entre dos puntos

        PARAMETROS:
        ___________
        Q: Punto
            Punto con el que se quiere calcular el punto medio
        RETURN:
        _______
        Punto
            Punto medio entre los dos puntos

        >>> P1 = Punto(0, 0)
        >>> P2 = Punto(2, 2)
        >>> M = P1.medio(P2)
        >>> M.x
        1.0
        >>> M.y
        1.0
        """
        x_medio = (self.x + Q.x) / 2
        y_medio = (self.y + Q.y) / 2
        return Punto(x_medio, y_medio)

    def __eq__(self, other):
        """
        Sobrecarga del operador == para puntos

        PARAMETROS:
        ___________
        other: Punto
            Punto con el que se quiere comparar
        RETURN:
        _______
        bool
            True si los puntos son iguales, False en caso contrario

        >>> p = Punto(0, 0)
        >>> q = Punto(0, 0)
        >>> r = Punto(1, 0)
        >>> p == q
        True
        >>> p == r
        False
        """
        return self.x == other.x and self.y == other.y

    def get_coord_cartesianas(self):
        """
        Metodo para obtener las coordenadas cartesianas (x, y)

        RETURN:
        _______
        tuple
            Coordenadas cartesianas del punto

        >>> P = Punto(4.0, 5.0)
        >>> P.get_coord_cartesianas()
        (4.0, 5.0)
        """
        return (self.x, self.y)

    def get_coord_polares(self):
        """
        Metodo para obtener las coordenadas polares (r, theta) del punto (x, y) -> (r, theta)
        donde r = sqrt(x^2 + y^2) y theta = atan(y/x), con x > 0, y > 0 -> 0 < theta < pi/2
        r es el modulo del punto y theta es el ángulo en radianes
        Aprovecha el metodo modulo() y usa funciones de la clase math

        >>> P = Punto(0.0, 1.0)
        >>> P.get_coord_polares()
        (1.0, 1.5707963267948966)
        """
        from math import atan, pi

        r = self.modulo()  # Módulo del punto usando el método modulo
        theta = atan(self.y / self.x) if self.x != 0 else (pi / 2) #Ángulo en radianes
        return (r, theta)
    
    def __neg__(self):
        """
        Sobrecarga del operador - (negación) para puntos (x, y) -> (-x, -y)

        RETURN:
        _______
        Punto
            Punto con las coordenadas negadas

        >>> P = Punto(2, 3)
        >>> Q = Punto(-2, -3)
        >>> -P == Q
        True
        """
        return Punto(-self.x, -self.y)

    def __add__(self, Q):
        """
        Sobrecarga del operador + (suma) para puntos
        Equivale a sumar los vectores formados por los puntos y obtener el punto resultante

        PARAMETROS:
        ___________
        Q: Punto
            Punto a sumar
        RETURN:
        _______
        Punto
            Punto resultante de la suma

        >>> P = Punto(1.0, 1.2)
        >>> Q = Punto(-2.4, 5.9)
        >>> S = P + Q
        >>> round(S.x, 1)
        -1.4
        >>> round(S.y, 1)
        7.1
        """
        return Punto(self.x + Q.x, self.y + Q.y)

    def __mul__(self, n):
        """
        Sobrecarga del operador * (producto) para puntos
        Equivale a multiplicar el módulo del punto por un número n y obtener el punto resultante

        PARAMETROS:
        ___________
        n: float
            Numero por el que se quiere multiplicar el punto
        RETURN:
        _______
        Punto
            Punto resultante de la multiplicacion

        >>> P = Punto(1.0, 1.2)
        >>> print(P * 3.0)
        (3.0,3.6)
        """
        return Punto(round(n * self.x, 1), round(n * self.y, 1))

if __name__ == '__main__':
    import doctest

    print(doctest.testmod(verbose=True))
