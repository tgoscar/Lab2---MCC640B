# Factorización de Enteros
## Algoritmos de Fermat y Reducción por Raíz Cuadrada
**Criptografía — Implementación según clase**
**Repositorio — https://github.com/tgoscar/Lab2---MCC640B**
---

## 01 — Descripción

| Algoritmo | Idea principal |
|-----------|---------------|
| **Fermat** | Busca `x` tal que `x² − n` sea cuadrado perfecto. Eficiente cuando `|p − q|` es pequeño. |
| **Raíz Cuadrada** | Explota `x² ≡ y² (mod n)` y calcula `mcd(x ± y, n)` para obtener factores no triviales. |

### Identidades clave

    Fermat:        n  =  x² - y²  =  (x-y)(x+y)
                   p  =  x - y  ,   q  =  x + y

    Raíz Cuad.:    x²  ≡  y²  (mod n)
                   =>  mcd(x - y, n)  y  mcd(x + y, n)  dan factores

---

## 02 — Código fuente

### Utilidades

```python
import math

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
```

### Fermat

```python
def fermat_factor(n, verbose=True):
    if n < 4: return None
    if n % 2 == 0: return 2, n // 2
    x = isqrt(n)
    if x * x < n: x += 1
    steps = 0
    limit = (n + 1) // 2
    while x <= limit:
        y2 = x * x - n
        is_sq, y = is_perfect_square(y2)
        if is_sq:
            p, q = x - y, x + y
            if verbose:
                print(f"  p={p}, q={q}  =>  {p}x{q}={p*q}  [OK]")
            return p, q
        x += 1
        steps += 1
    return None
```

### Reducción Raíz Cuadrada

```python
def sqrt_reduction_factor(n, verbose=True):
    if n < 4: return None
    if n % 2 == 0: return 2, n // 2
    a = isqrt(n)
    if a * a < n: a += 1
    while a <= n:
        b2 = a * a - n
        is_sq, b = is_perfect_square(b2)
        if is_sq and b != 0:
            g1 = mcd(a - b, n)
            g2 = mcd(a + b, n)
            if 1 < g1 < n: return g1, n // g1
            if 1 < g2 < n: return g2, n // g2
        a += 1
    return None
```

---

## 03 — Outputs

**n = 5959 — Fermat (3 pasos):**

    paso 1: x=78, x²-n=125, y=11
    paso 2: x=79, x²-n=282, y=16
    paso 3: x=80, x²-n=441, y=21  <-- cuadrado perfecto!
    p=59, q=101  =>  59x101=5959  [OK]

**n = 5959 — Raíz Cuadrada:**

    a=80: b²=441 --> b=21  OK
    mcd(59,  5959) = 59
    mcd(101, 5959) = 101
    p=59, q=101  [OK]

**n = 8051 — Fermat (1 paso):**

    paso 1: x=90, x²-n=49, y=7  <-- cuadrado perfecto!
    p=83, q=97  =>  83x97=8051  [OK]

---

## 04 — Experimentos

| n | descripción | p | q | resultado |
|------:|-------------|---:|---:|:---------:|
| 5 959 | p y q cercanos | 59 | 101 | OK |
| 8 051 | p y q cercanos | 83 | 97 | OK |
| 10 403 | p y q cercanos | 101 | 103 | OK |
| 3 599 | p y q cercanos | 59 | 61 | OK |
| 1 517 | diferencia media | 37 | 41 | OK |
| 2 021 | diferencia media | 43 | 47 | OK |
| 15 251 | semiprimos | 101 | 151 | OK |

---

## 05 — Conclusión

- Fermat converge en 1 paso cuando `p ≈ q ≈ √n`
- Raíz cuadrada obtiene los mismos factores vía `mcd(a±b, n)`
- Ambos degradan cuando `|p − q|` es grande
- No son prácticos para `n > 60 bits`

---

## Convertir a PDF

```bash
pandoc Factorizacion_Fermat.md -o reporte.pdf --pdf-engine=xelatex
```
