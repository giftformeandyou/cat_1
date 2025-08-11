def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

n = int(input("Введите количество чисел Фибоначчи: "))
if n > 0:
    result = fibonacci(n)
    print(f"Первые {n} чисел Фибоначчи: {result}")
else:
    print("Введите число больше 0")