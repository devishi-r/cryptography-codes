def power(a, b, p):
    result = 1
    a = a % p  # Update a if a >= p

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        b = b // 2
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_primitive_root(g, p):
    result = 1
    for i in range(1, p):
        result = (result * g) % p
        if result == 1 and i < p - 1:
            return False
    return True

def input_number(prompt, condition):
    while True:
        try:
            n = int(input(prompt))
            if condition(n):
                return n
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Input P
    P = input_number("Enter a prime number P: ", is_prime)
    print("The value of P:", P)

    # Input G
    def g_condition(g):
        return 1 < g < P and is_primitive_root(g, P)

    G = input_number(f"Enter primitive root G (1 < G < {P}): ", g_condition)
    print("The value of G:", G)

    # Private key for Alice
    a = int(input("Enter private key for Alice: "))
    print("The private key a for Alice:", a)
    x = power(G, a, P)  # Public key sent by Alice

    # Private key for Bob
    b = int(input("Enter private key for Bob: "))
    print("The private key b for Bob:", b)
    y = power(G, b, P)  # Public key sent by Bob

    # Secret keys
    ka = power(y, a, P)  # Alice's secret
    kb = power(x, b, P)  # Bob's secret

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()
