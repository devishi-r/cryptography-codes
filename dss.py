import random

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def dss():
    # Get inputs from user
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    message = input("Enter original message: ")
    x = int(input("Enter private key x: "))
    k = int(input("Enter random integer k: "))
    h = int(input("Enter hash value h: "))

    # Key Generation
    g = 2  # Simple generator, can be changed
    y = pow(g, x, p)

    print("\nSender side:")
    print(f"Public key y: {y}")

    # Signature Generation
    r = (pow(g, k, p) % q)
    k_inv = mod_inverse(k, q)
    s = (k_inv * (h + x * r)) % q

    print(f"r: {r}")
    print(f"s: {s}")

    # Receiver side
    print("\nReceiver side:")
    w = mod_inverse(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    print(f"z: {h}")  # z is the same as h in this case
    print(f"u1: {u1}")
    print(f"u2: {u2}")
    print(f"v: {v}")
    print(f"Signature verified: {v == r}")

# Run the function
dss()
