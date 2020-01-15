#ClassRoom_2247

T = [[1, 1], [1, 0]]
mat = [[1, 0], [1, 0]]


def multiply(T, F):
    a = T[0][0] * F[0][0] + T[0][1] * F[1][0]
    b = T[0][0] * F[0][1] + T[0][1] * F[1][1]
    c = T[1][0] * F[0][0] + T[1][1] * F[1][0]
    d = T[1][0] * F[0][1] + T[1][1] * F[1][1]

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
        return res[0][0], res[1][0]

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    x = arr[0] + 1
    y = arr[1] + 1
    n = arr[2]
    # print(x, y, n)
    p1, p2 = fibonacci(n-2)
    print(p1, p2)
    result = (x ** p2) * (y ** p1)
    print(result - 1)
