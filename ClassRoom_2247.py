# ClassRoom_2247

T = [[1, 1], [1, 0]]
mat = [[1, 0], [1, 0]]
mod = 1000000006


def multiply(T, F):
    a = (((T[0][0] % mod) * (F[0][0] % mod)) % mod + ((T[0][1] % mod) * (F[1][0] % mod)) % mod) % mod
    b = (((T[0][0] % mod) * (F[0][1] % mod)) % mod + ((T[0][1] % mod) * (F[1][1] % mod)) % mod) % mod
    c = (((T[1][0] % mod) * (F[0][0] % mod)) % mod + ((T[1][1] % mod) * (F[1][0] % mod)) % mod) % mod
    d = (((T[1][0] % mod) * (F[0][1] % mod)) % mod + ((T[1][1] % mod) * (F[1][1] % mod)) % mod) % mod

    return [[a, b], [c, d]]


def power(T, n):
    if n == 1:
        return T
    else:
        F = power(T, n // 2)
        F = multiply(F, F)
        if n % 2 != 0:
            F = multiply(F, T)

        return F


def fibonacci(n):
    if n == 0 or n == 1:
        return 1, 1
    else:
        z = power(T, n)
        res = multiply(z, mat)
        return res[0][0] % mod, res[1][0] % mod


def modIt(v, p):
    if p == 0:
        return 1
    if p % 2 != 0:
        return ((v % (mod + 1)) * (modIt((v * v) % (mod + 1), p // 2))) % (mod + 1)
    else:
        return modIt(v * v % (mod + 1), p // 2)


t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    x = (arr[0] + 1) % (mod + 1)
    y = (arr[1] + 1) % (mod + 1)
    n = (arr[2]) % (mod + 1)
    p1, p2 = fibonacci(n - 2)
    result = ((modIt(x, p2) % (mod + 1)) * (modIt(y, p1) % (mod + 1))) % (mod + 1)
    alpha = (result - 1) % (mod + 1)
    print(alpha)
