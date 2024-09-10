# Lembrando que os números negativos não fazem parte da sequência de Fibonacci!
def Seq_fibonacci(num):
    if num < 0:
        return False   

    fib1, fib2 = 0, 1
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
    return fib2 == num

def main():
    while True:
        usuario = input("Por favor, Digite um número ou se deseja digite 'sair' para encerrar): ")

        if usuario.lower() == 'sair':
            print("Programa encerrado.")
            break

        try:
            num = int(usuario)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            continue

        if Seq_fibonacci(num):
            print(f"O número {num} faz parte da sequência de Fibonacci.")
        else:
            print(f"O número {num} não faz parte da sequência de Fibonacci.")

if __name__ == "__main__":
    main()
