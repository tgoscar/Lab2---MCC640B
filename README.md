Factorización de Enteros — Fermat y Reducción de Raíz Cuadrada
Implementación de dos algoritmos clásicos de factorización de enteros desarrollados en clase de Criptografía.

Algoritmos implementados
1. Factorización de Fermat
Basado en la identidad:
n = x² - y² = (x - y)(x + y)   =>   p = x - y,  q = x + y
Pasos del algoritmo (según clase):

Iniciar con x = ⌈√n⌉
Calcular y² = x² − n
Verificar si y² es cuadrado perfecto → y = √(y²)
Si x ≡ ±y (mod n) → factor trivial, incrementar x y repetir
Si no → p = x − y, q = x + y, retornar factores


Eficiencia: muy rápido cuando |p − q| es pequeño (p y q cercanos a √n). En el peor caso degenera a fuerza bruta.


2. Factorización por Reducción de Raíz Cuadrada
Basado en la congruencia:
x² ≡ y² (mod n)   =>   mcd(x ± y, n) da factor no trivial
Pasos del algoritmo:

Buscar a, b tales que b² = a² − n (cuadrado perfecto)
Calcular g₁ = mcd(a − b, n) y g₂ = mcd(a + b, n)
Si 1 < g₁ < n → factor encontrado: p = g₁, q = n / g₁
Si el factor es trivial (1 o n) → incrementar a y repetir


Resultados experimentales
npqFermat (pasos)Raíz Cuadrada (pasos)5 95959101338 05183971110 403101103111 5173741333 599596133

Ambos algoritmos convergen en pocos pasos cuando p y q son cercanos entre sí.


Uso
bashpython3 factorizacion_fermat.py
Ejemplo de salida
[Fermat] n = 5959
  Inicio: x = ceil(sqrt(5959)) = 78
  paso    1: x=78,  x^2-n=125,  y=11
  paso    2: x=79,  x^2-n=282,  y=16
  paso    3: x=80,  x^2-n=441,  y=21  <-- cuadrado perfecto!

  Exito en 3 pasos!
  p = x - y = 59
  q = x + y = 101
  Verificacion: 59 x 101 = 5959  OK

[Reduccion Raiz] n = 5959
  Congruencia: a=80, b=21
  mcd(a-b, n) = mcd(59, 5959) = 59
  mcd(a+b, n) = mcd(101, 5959) = 101
  Factor: p=59, q=101  OK
Uso como módulo
pythonfrom factorizacion_fermat import fermat_factor, sqrt_reduction_factor

p, q = fermat_factor(8051, verbose=False)
print(p, q)  # 83 97

p, q = sqrt_reduction_factor(5959, verbose=False)
print(p, q)  # 59 101

Estructura del proyecto
.
├── factorizacion_fermat.py   # Implementación de ambos algoritmos
└── README.md                 # Este archivo

Complejidad
AlgoritmoMejor casoPeor casoFermatO(1) cuando p ≈ q ≈ √nO(n) cuando p = 2Reducción √O(1) con congruencia inmediataO(n)

Referencias

Menezes, A., van Oorschot, P., Vanstone, S. — Handbook of Applied Cryptography, Cap. 3
Pomerance, C. — A Tale of Two Sieves (1996)
Apuntes de clase — Criptografía


Requisitos

Python 3.8+
Sin dependencias externas (solo math de la stdlib)
