import math


class CalculadoraRaizCuadrada:
    def calcular_raiz(self, numero: float) -> float:
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(numero)

    def mostrar_raiz(self, numero: float):
        try:
            raiz = self.calcular_raiz(numero)
            print(f"La raíz cuadrada de {numero} es {raiz:.4f}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    # Ejemplo de uso
    numero = float(input("Ingrese un número: "))

    calculadora = CalculadoraRaizCuadrada()
    calculadora.mostrar_raiz(numero)
