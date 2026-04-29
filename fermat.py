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

