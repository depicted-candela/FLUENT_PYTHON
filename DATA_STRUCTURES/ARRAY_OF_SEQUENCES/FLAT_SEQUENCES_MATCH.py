"""Ejemplo de Comparador de Secuencias Planas
"""
class PaisNumeroTelefonico:
    """Comparador de secuencias planas
    """
    def __init__(self, numero : str):
        """Constructor de para determinar el país de un número telefónico dado
        Args:
            numero (str): Número del cuál se determina su país origen
        >>> _ = PaisNumeroTelefonico('573208639711')
        573208639711 es un número telefónico Colombiano
        >>> _ = PaisNumeroTelefonico('57320863971')
        AssertionError: Ese número telefónico no lo registra ningún país
        """
        match tuple(numero):
            case ['5', '7', *rest] if len(rest) == 10: print(f"{numero} es un número telefónico Colombiano")
            case ['5', '2', *rest] if len(rest) == 10: print(f"{numero} es un número telefónico Mexicano")
            case ['1', *rest] if len(rest) == 10: print(f"{numero} es un número telefónico estadounidense")
            case _: assert False, "Ese número telefónico no lo registra ningún país"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    PaisNumeroTelefonico('573208639711')