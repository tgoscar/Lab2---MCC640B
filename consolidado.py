"""
Factorizacion de Enteros - Fermat y Reduccion de Raiz Cuadrada
==============================================================
Criptografia - Implementacion segun clase

Algoritmos:
  1. Factorizacion de Fermat         (eficiente cuando p y q son cercanos)
  2. Reduccion de Raiz Cuadrada      (basado en x^2 = y^2 mod n)

Uso:
    python3 factorizacion_fermat.py

    O como modulo:
        from factorizacion_fermat import fermat_factor, sqrt_reduction_factor
        p, q = fermat_factor(5959)
"""

import math


# ------------------------------------------------------------------
# Utilidades
# ------------------------------------------------------------------

def isqrt(n):
    return math.isqrt(n)

def is_perfect_square(n):
    if n < 0:
        return False, 0
    r = isqrt(n)
    return (r * r == n), r

def mcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# ------------------------------------------------------------------
# Algoritmo 1 - Factorizacion de Fermat
# ------------------------------------------------------------------

def fermat_factor(n, verbose=True):
    if n < 4:
        return None
    if n % 2 == 0:
        return 2, n // 2

    x = isqrt(n)
    if x * x < n:
        x += 1

    if verbose:
        print(f"\n{'─'*50}\n  FERMAT  |  n = {n}\n{'─'*50}")
        print(f"  Inicio: x = ceil(sqrt({n})) = {x}\n")

    steps = 0
    limit = (n + 1) // 2

    while x <= limit:
        y2 = x * x - n
        is_sq, y = is_perfect_square(y2)

        if verbose and steps < 12:
            mark = "  <-- cuadrado perfecto!" if is_sq else ""
            print(f"  paso {steps+1:>4}: x={x:>10},  x^2-n={y2:>12},  y={y}{mark}")
        elif verbose and steps == 12:
            print("  ...")

        if is_sq:
            p, q = x - y, x + y
            if verbose:
                print(f"\n  Exito en {steps+1} paso(s).")
                print(f"  p = x - y = {p}")
                print(f"  q = x + y = {q}")
                print(f"  Verificacion: {p} x {q} = {p*q}  {'[OK]' if p*q==n else '[ERROR]'}")
            return p, q

        x += 1
        steps += 1

    if verbose:
        print("  Sin factores - n posiblemente primo.")
    return None


# ------------------------------------------------------------------
# Algoritmo 2 - Reduccion de Raiz Cuadrada
# ------------------------------------------------------------------

def sqrt_reduction_factor(n, verbose=True):
    if n < 4:
        return None
    if n % 2 == 0:
        return 2, n // 2

    a = isqrt(n)
    if a * a < n:
        a += 1

    if verbose:
        print(f"\n{'─'*50}\n  REDUCCION RAIZ  |  n = {n}\n{'─'*50}")
        print(f"  Buscar a,b: b^2 = a^2 - n  (x^2 = y^2 mod n)")
        print(f"  Inicio: a = ceil(sqrt({n})) = {a}\n")

    steps = 0

    while a <= n:
        b2 = a * a - n
        is_sq, b = is_perfect_square(b2)

        if verbose and steps < 12:
            mark = f"  --> b = {b}  OK" if is_sq else ""
            print(f"  a={a:>10}:  b^2 = {b2:>12}{mark}")
        elif verbose and steps == 12:
            print("  ...")

        if is_sq and b != 0:
            g1 = mcd(a - b, n)
            g2 = mcd(a + b, n)

            if verbose:
                print(f"\n  Congruencia: a={a}, b={b}")
                print(f"  mcd(a-b, n) = mcd({a-b}, {n}) = {g1}")
                print(f"  mcd(a+b, n) = mcd({a+b}, {n}) = {g2}")

            if 1 < g1 < n:
                p, q = g1, n // g1
                if verbose:
                    print(f"  p = {p},  q = {q}")
                    print(f"  Verificacion: {p} x {q} = {p*q}  {'[OK]' if p*q==n else '[ERROR]'}")
                return p, q

            if 1 < g2 < n:
                p, q = g2, n // g2
                if verbose:
                    print(f"  p = {p},  q = {q}")
                    print(f"  Verificacion: {p} x {q} = {p*q}  {'[OK]' if p*q==n else '[ERROR]'}")
                return p, q

            if verbose:
                print("  Factor trivial, continuando...")

        a += 1
        steps += 1

    if verbose:
        print("  Sin factores no triviales.")
    return None


# ------------------------------------------------------------------
# Experimentos
# ------------------------------------------------------------------

def experimentos():
    casos = [
        ("p y q cercanos",   5959,  59, 101),
        ("p y q cercanos",   8051,  83,  97),
        ("p y q cercanos",  10403, 101, 103),
        ("p y q cercanos",   3599,  59,  61),
        ("diferencia media", 1517,  37,  41),
        ("diferencia media", 2021,  43,  47),
        ("semiprimos",      15251, 101, 151),
    ]

    for titulo, func in [("Fermat", fermat_factor), ("Reduccion Raiz Cuadrada", sqrt_reduction_factor)]:
        print(f"\n{'='*62}\n  EXPERIMENTOS - {titulo}\n{'='*62}")
        print(f"  {'n':>8}  {'descripcion':<20}  {'p':>6}  {'q':>6}  resultado")
        print("  " + "-"*58)
        for desc, n, *_ in casos:
            r = func(n, verbose=False)
            if r:
                p, q = r
                print(f"  {n:>8}  {desc:<20}  {p:>6}  {q:>6}  {'[OK]' if p*q==n else '[ERROR]'}")
            else:
                print(f"  {n:>8}  {desc:<20}  {'—':>6}  {'—':>6}  [sin factores]")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

if __name__ == "__main__":
    fermat_factor(5959)
    sqrt_reduction_factor(5959)

    fermat_factor(8051)
    sqrt_reduction_factor(8051)

    experimentos()
