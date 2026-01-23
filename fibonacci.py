n = int(input("Enter the value of n: "))

a, b = 0, 1
fib_sum = 0

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    fib_sum += a
    a, b = b, a + b

print("\nSum of Fibonacci numbers:", fib_sum)
