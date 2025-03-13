 #Prueba de que se ha commited y pusheado bien en GitHub

from Punto import * #poniendo asterisco nos sirve para no tener que llamar la función Punto cada vez ej. Punto.Punto(1.0, 2.0)

class Recta:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2
        self._m = None  # Almacenamos la pendiente
        self._b = None  # Almacenamos la ordenada al origen
        self._calcular_pendiente_y_ordenada()  # Calculamos al inicializar

    def _calcular_pendiente_y_ordenada(self):
        if self.P1.x() == self.P2.x():
            self._m = float('inf')
            self._b = None
        else:
            self._m = (self.P2.y - self.P1.y) / (self.P2.x() - self.P1.x())
            self._b = self.P1.y - self._m * self.P1.x()

    def __str__(self):
        """
        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(4.0, 2.0)
        >>> R = Recta(P, Q)
        >>> print(R)
        (1.0,2.0)-(4.0,2.0)
        """
        return str(self.P1) + '-' + str(self.P2)

    def m(self):
        return self._m

    def b(self):
        return self._b

    def perpendicular(self, punto):
        """
        >>> P = Punto(1.0, 2.0)
        >>> Q = Punto(4.0, 6.0)
        >>> R = Recta(P, Q)
        >>> S = Punto(2.0, 3.0)
        >>> recta_perp = R.perpendicular(S)
        >>> abs(recta_perp.m() * R.m() + 1) < 1e-10
        True
        """
        # Si la recta original es vertical, la perpendicular es horizontal
        if self.P1.x() == self.P2.x():
            punto_segundo = Punto(punto.x() + 1, punto.y)
            return Recta(punto, punto_segundo)

        # Si la recta original es horizontal, la perpendicular es vertical
        if self.P1.y == self.P2.y:
            punto_segundo = Punto(punto.x(), punto.y + 1)
            return Recta(punto, punto_segundo)

        # En otros casos, la pendiente de la perpendicular es -1/m
        pendiente_perp = -1 / self.m()

        # Calculamos un segundo punto usando la pendiente
        # y' = y + pendiente_perp * (x' - x)
        # Elegimos x' = x + 1
        x_segundo = punto.x() + 1
        y_segundo = punto.y + pendiente_perp * (x_segundo - punto.x())
        punto_segundo = Punto(x_segundo, y_segundo)

        return Recta(punto, punto_segundo)

    def interseccion(self, Recta):
        """"
        >>> P1 = Punto(0.0, 0.0)
        >>> P2 = Punto(2.0, 2.0)
        >>> R1 = Recta(P1, P2)  # y = x
        >>> P3 = Punto(0.0, 4.0)
        >>> P4 = Punto(4.0, 0.0)
        >>> R2 = Recta(P3, P4)  # y = -x + 4
        >>> P_int = R1.interseccion(R2)
        >>> print(P_int)
        (2.0,2.0)

        >>> P5 = Punto(1.0, 0.0)
        >>> P6 = Punto(1.0, 5.0)
        >>> R3 = Recta(P5, P6)  # Recta vertical x = 1
        >>> P_int2 = R1.interseccion(R3)
        >>> print(P_int2)
        (1.0,1.0)

        >>> P7 = Punto(0.0, 3.0)
        >>> P8 = Punto(5.0, 3.0)
        >>> R4 = Recta(P7, P8)  # Recta horizontal y = 3
        >>> P_int3 = R3.interseccion(R4)
        >>> print(P_int3)
        (1.0,3.0)

        >>> P9 = Punto(2.0, 0.0)
        >>> P10 = Punto(2.0, 5.0)
        >>> R5 = Recta(P9, P10)  # Recta vertical x = 2
        >>> R6 = Recta(P9, P10)  # Otra recta igual
        >>> P_int4 = R5.interseccion(R6)  # Rectas coincidentes
        >>> P_int4 is None
        True
        """
        # Caso 1: Si ambas rectas son verticales (x constante)
        if self.P1.x() == self.P2.x() and Recta.P1.x() == Recta.P2.x():
            # Si tienen el mismo valor de x, son coincidentes (o la misma)
            if self.P1.x() == Recta.P1.x():
                return None  # Rectas coincidentes, no hay un punto de intersección único
            else:
                return None  # Rectas paralelas, no hay intersección

        # Caso 2: Si esta recta es vertical
        if self.P1.x() == self.P2.x():
            # La otra recta no es vertical (ya lo verificamos en el Caso 1)
            x_interseccion = self.P1.x()
            m2 = Recta.m()
            b2 = Recta.b()
            y_interseccion = m2 * x_interseccion + b2
            return Punto(x_interseccion, y_interseccion)

        # Caso 3: Si la otra recta es vertical
        if Recta.P1.x() == Recta.P2.x():
            x_interseccion = Recta.P1.x()
            m1 = self.m()
            b1 = self.b()
            y_interseccion = m1 * x_interseccion + b1
            return Punto(x_interseccion, y_interseccion)

        # Caso 4: Ninguna de las rectas es vertical
        m1 = self.m()
        b1 = self.b()
        m2 = Recta.m()
        b2 = Recta.b()

        # Si las pendientes son iguales, las rectas son paralelas o coincidentes
        if m1 == m2:
            # Si los interceptos son iguales, las rectas son coincidentes
            if b1 == b2:
                return None  # Rectas coincidentes
            else:
                return None  # Rectas paralelas

        # Calcular el punto de intersección
        # Resolvemos el sistema de ecuaciones:
        # y = m1*x + b1
        # y = m2*x + b2
        # Igualando: m1*x + b1 = m2*x + b2
        # Despejamos x: x = (b2 - b1) / (m1 - m2)
        x_interseccion = (b2 - b1) / (m1 - m2)
        # Sustituimos x en cualquiera de las ecuaciones para obtener y
        y_interseccion = m1 * x_interseccion + b1

        return Punto(x_interseccion, y_interseccion)

    def distancia(self, punto): #No ponemos el parámetro recta porque es el self
        """
        >>> P1 = Punto(0.0, 0.0)
        >>> P2 = Punto(0.0, 5.0)
        >>> R = Recta(P1, P2)
        >>> P3 = Punto(3.0, 4.0)
        >>> R.distancia(P3)
        3.0
        """
        # Caso especial: recta vertical
        if self.P1.x() == self.P2.x():
            # Para una recta vertical, la distancia es la diferencia en x
            return abs(punto.x() - self.P1.x())

        # Caso especial: recta horizontal
        if self.P1.y == self.P2.y:
            # Para una recta horizontal, la distancia es la diferencia en y
            return abs(punto.y - self.P1.y)

        # Caso general: usar la fórmula de distancia de un punto a una recta
        # Distancia = |Ax + By + C| / sqrt(A² + B²)
        # Donde Ax + By + C = 0 es la ecuación de la recta

        # Convertimos y = mx + b a la forma general Ax + By + C = 0
        # y - mx - b = 0
        # -mx + y - b = 0
        # Entonces A = -m, B = 1, C = -b

        pendiente = self.m()
        b_valor = self.b()

        A = -pendiente
        B = 1
        C = -b_valor

        # Aplicamos la fórmula
        numerador = abs(A * punto.x() + B * punto.y + C)
        denominador = (A ** 2 + B ** 2) ** 0.5

        return numerador / denominador

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=False))

    P = Punto(1.0, 2.0)
    Q = Punto(2.0, 5.0)
    S = Punto(3.0, 7.0)
    R = Recta(P, Q)

    pendiente = R.m()
    ordenada = R.b()
    perpendicular = R.perpendicular(S)
    interseccion = R.interseccion(perpendicular)
    distancia = R.distancia(S)
    print("Datos sobre la recta que pasa por P y Q:",
          '\nPendiente:', pendiente,
          '\nOrdenada al origen:', ordenada,
          '\nRecta perpendicular a R que pasa por S:', perpendicular,
          '\nPunto de intersección entre las perpendiculares:', interseccion,
          '\nDistancia entre R y S:', distancia
          )
