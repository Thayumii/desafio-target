def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0 # Verificar se o número pertence a sequência.


numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence a sequência de Fibonacci.")
else:    
    print(f"O número {numero} não pertence a sequência de Fibonacci.")