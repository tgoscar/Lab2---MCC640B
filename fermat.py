# ── Algoritmo de Fermat ──────────────────────────────────────
function fermat_factor(n):
    x = ceil(sqrt(n))         # comenzar desde ⌈√n⌉
    while x <= (n + 1) / 2:
        y2 = x*x - n
        y  = sqrt(y2)
        if y*y == y2:           # y2 es cuadrado perfecto
            p = x - y
            q = x + y
            return p, q           # n = p × q
        x += 1
    return None               # n es primo

# ── Factorización por Reducción de Raíz Cuadrada ─────────────
# Basado en: si x² ≡ y² (mod n) entonces mcd(x±y, n) da factor
function sqrt_reduction_factor(n):
    # Paso 1: Pasos de Fermat para hallar congruencias
    for a in range(ceil(sqrt(n)), n):
        b2 = a*a - n
        if is_perfect_square(b2):
            b = sqrt(b2)
            if a != b:
                p = mcd(a - b, n)
                q = mcd(a + b, n)
                if 1 < p < n:
                    return p, q
    return None
