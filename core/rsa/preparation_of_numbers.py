import random
import sys



def HOD(mass_abqr, a, b, sum_try):
    q = int(a / b)
    r = a - b * q
    sum_try += 1
    mass_abqr.append([a, b, q, r])
    if r == 0:
        return mass_abqr, sum_try
    else:
        return HOD(mass_abqr, b, r, sum_try)


def x_y(mass_xy, start_alg, sum_try, final_mass_abqr):
    if start_alg <= sum_try:
        x = mass_xy[start_alg - 2][0] - ((final_mass_abqr[start_alg - 1][2]) * mass_xy[start_alg - 1][0])
        y = mass_xy[start_alg - 2][1] - ((final_mass_abqr[start_alg - 1][2]) * mass_xy[start_alg - 1][1])
        start_alg += 1
        mass_xy.append([x, y])
        return x_y(mass_xy, start_alg, sum_try, final_mass_abqr)
    else:
        return mass_xy


def rashirenii_alg_evclid(func_eiler, e):
    mass_abqr = [[func_eiler, e, 0, 0]]
    mass_xy = [[1, 0], [0, 1]]
    sum_try = 0
    start_alg = 2

    final_mass_abqr, sum_try = HOD(mass_abqr, mass_abqr[0][0], mass_abqr[0][1], sum_try)

    mass_xy = x_y(mass_xy, start_alg, sum_try, final_mass_abqr)

    if mass_xy[-1][1] < 0:
        return func_eiler + mass_xy[-1][1]
    else:
        return mass_xy[-1][1]


def eratosfen():
    mass = [2]
    n = 5000
    m = (n - 1) // 2
    b = [True] * m
    i, p = 0, 3
    while p * p < n:
        if b[i]:
            mass.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            mass.append(p)
        i += 1
        p += 2
    return mass


def proverka_na_prostih(n):
    mass = eratosfen()
    for elem in mass:
        if n % elem == 0:
            return False
        else:
            continue
    else:
        return True


def rabin_miller(n):
    n = n
    s = 0
    d = 0
    buf = n - 1
    while buf != 0:
        if buf % 2 == 0:
            buf = buf / 2
            s += 1
        else:
            d = int(buf)
            break

    response = True
    for i in range(0, 6):
        a = random.randint(3, 100)
        if pow(a, d, n) == (1 % n):  # if ((a ** d) % n) == (1 % n):
            response = True
        else:
            for j in range(s):
                # if ((a ** ((2 ** i) * d)) % n) == (-1 % n):
                if pow(a, (pow(2, i) * d), n) == (-1 % n):
                    response = True
                    break
                else:
                    continue
            else:
                response = False
                break
    if not response:
        return False
    else:
        return True


def simplicity_test(n):
    if proverka_na_prostih(n):
        if rabin_miller(n):
            return n
        else:
            return simplicity_test(n + 2)
    else:
        return simplicity_test(n + 2)


def generate():
    n = random.randint(1000000000, 10000000000)
    if n % 2 == 0:
        return generate()  
    else:
        return n  


def scan_prime_number():
    n = generate()
    return simplicity_test(n)


def main_func():
    p = scan_prime_number()
    q = scan_prime_number()

    func_eiler = (int(p) - 1) * (int(q) - 1)
    e = 7
    d = rashirenii_alg_evclid(func_eiler, e)
    if d == 1:
        return main_func()
    else:
        return [e, d, int(p) * int(q)]
