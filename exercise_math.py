def math():
    a = 57
    b = 7

    results = [
        a + b,
        a - b,
        a * b,
        (a + b) / 2,
        int(a / b),
        int(a % b),
        a / b,
    ]

    for e in results:
        print(e)
