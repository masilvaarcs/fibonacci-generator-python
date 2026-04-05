"""Gerador para calcular a série de Fibonacci usando generators do Python."""


def fibonacci_generator():
    """Gerador infinito da sequência de Fibonacci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_list(n: int) -> list:
    """Retorna os primeiros n números de Fibonacci."""
    gen = fibonacci_generator()
    return [next(gen) for _ in range(n)]


def main():
    gen = fibonacci_generator()
    print("Primeiros 50 números de Fibonacci:")
    for _ in range(50):
        print(next(gen), end=" ")
    print()


if __name__ == "__main__":
    main()
