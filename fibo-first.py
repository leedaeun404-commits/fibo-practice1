def fibonacci_sequence(k):
    if k < 2:
        return k
    return fibonacci_sequence(k - 1) + fibonacci_sequence(k - 2)


if __name__ == "__main__":
    print(fibonacci_sequence(10))
