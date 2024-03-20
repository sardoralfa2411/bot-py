# Funksiya f(x) = x^3 - 0.1x^2 + 0.4x - 1.5 ni hisoblash
def f(x):
    return x**3 - 0.1*x**2 + 0.4*x - 1.5
# Funksiya f(x) ning ildizini topish
def iterative_method(epsilon=0.01):
    x = 0.0  # Boshlanish nuqtasi
    # Iteratsiya
    while True:
        h = f(x) / (3*x**2 - 0.2*x + 0.4)  # Iteratsiya formulasi
        x -= h  # Yangilash
        # Agar h kichik epsilondan ham kichik bo'lsa, siklni to'xtatamiz
        if abs(h) < epsilon:
            break
    return x
# ildizning taqribiy qiymatini hisoblash
result = iterative_method(epsilon=0.01)
print("Tenglama yechimi: x =", result)
