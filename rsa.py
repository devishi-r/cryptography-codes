def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # No inverse exists
    if t < 0:
        t += phi
    return t

def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def is_valid_e(e, phi):
    return 1 < e < phi and gcd(e, phi) == 1

def is_valid_d(d, e, phi):
    return (d * e) % phi == 1

def generate_keys():
    while True:
        try:
            p = int(input("Enter first prime number (p): "))
            q = int(input("Enter second prime number (q): "))

            if not is_prime(p) or not is_prime(q):
                print("Error: Both numbers must be prime!")
                continue

            n = p * q
            phi = (p - 1) * (q - 1)
            print("phi(n) =", phi)

            e = int(input("Choose e (1 < e < phi(n) and gcd(e, phi(n)) = 1): "))
            if not is_valid_e(e, phi):
                print("Error: Invalid value for e!")
                continue

            d = int(input("Choose d (d * e ≡ 1 (mod phi(n))): "))
            if not is_valid_d(d, e, phi):
                print("Error: Invalid value for d!")
                continue

            return e, d, n
        except ValueError:
            print("Error: Please enter valid integers.")

def encrypt(m, e, n):
    return mod_pow(m, e, n)

def decrypt(c, d, n):
    return mod_pow(c, d, n)

def main():
    e, d, n = generate_keys()

    print(f"\nPublic Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    try:
        m = int(input("\nEnter message (numeric value): "))
        if m >= n:
            print(f"Error: Message must be less than n = {n}")
            return

        print("Original Message:", m)
        c = encrypt(m, e, n)
        print("Encrypted Message:", c)
        decrypted = decrypt(c, d, n)
        print("Decrypted Message:", decrypted)
    except ValueError:
        print("Error: Please enter a valid numeric message.")

if __name__ == "__main__":
    main()
