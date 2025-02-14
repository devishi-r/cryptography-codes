import java.math.BigInteger;
import java.util.Scanner;

class Main {
    // Function to compute base^expo mod m using BigInteger
    static BigInteger power(BigInteger base, BigInteger expo, BigInteger m) {
        return base.modPow(expo, m);
    }

    // Function to find modular inverse of e modulo phi(n)
    static BigInteger modInverse(BigInteger e, BigInteger phi) {
        return e.modInverse(phi);
    }

    // Function to verify if a number is prime
    static boolean isPrime(BigInteger num) {
        return num.isProbablePrime(100);
    }

    // Function to check if e is valid
    static boolean isValidE(BigInteger e, BigInteger phi) {
        return e.compareTo(BigInteger.ONE) > 0 && 
               e.compareTo(phi) < 0 && 
               e.gcd(phi).equals(BigInteger.ONE);
    }

    // Function to check if d is valid
    static boolean isValidD(BigInteger d, BigInteger e, BigInteger phi) {
        return d.multiply(e).mod(phi).equals(BigInteger.ONE);
    }

    // RSA Key Generation with user input
    static void generateKeys(BigInteger[] keys, Scanner scanner) {
        while (true) {
            try {
                // Get p and q from user
                System.out.print("Enter first prime number (p): ");
                BigInteger p = new BigInteger(scanner.nextLine());
                
                System.out.print("Enter second prime number (q): ");
                BigInteger q = new BigInteger(scanner.nextLine());

                // Verify if numbers are prime
                if (!isPrime(p) || !isPrime(q)) {
                    System.out.println("Error: Both numbers must be prime!");
                    continue;
                }

                BigInteger n = p.multiply(q);
                BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));

                // Get e from user
                System.out.println("phi(n) = " + phi);
                System.out.print("Choose e (1 < e < phi(n) and gcd(e, phi(n)) = 1): ");
                BigInteger e = new BigInteger(scanner.nextLine());

                // Verify if e is valid
                if (!isValidE(e, phi)) {
                    System.out.println("Error: Invalid value for e!");
                    continue;
                }

                // Get d from user
                System.out.print("Choose d (d * e ≡ 1 (mod phi(n))): ");
                BigInteger d = new BigInteger(scanner.nextLine());

                // Verify if d is valid
                if (!isValidD(d, e, phi)) {
                    System.out.println("Error: Invalid value for d! It must satisfy d * e ≡ 1 (mod phi(n))");
                    continue;
                }

                keys[0] = e;  // Public Key (e)
                keys[1] = d;  // Private Key (d)
                keys[2] = n;  // Modulus (n)
                break;

            } catch (NumberFormatException ex) {
                System.out.println("Error: Please enter valid numbers!");
            }
        }
    }

    // Encrypt message using public key (e, n)
    static BigInteger encrypt(BigInteger m, BigInteger e, BigInteger n) {
        return power(m, e, n);
    }

    // Decrypt message using private key (d, n)
    static BigInteger decrypt(BigInteger c, BigInteger d, BigInteger n) {
        return power(c, d, n);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger[] keys = new BigInteger[3]; // e, d, n

        try {
            // Key Generation with user input
            generateKeys(keys, scanner);

            System.out.println("\nPublic Key (e, n): (" + keys[0] + ", " + keys[2] + ")");
            System.out.println("Private Key (d, n): (" + keys[1] + ", " + keys[2] + ")");

            // Get message from user
            System.out.print("\nEnter message (numeric value): ");
            BigInteger M = new BigInteger(scanner.nextLine());

            // Check if message is less than n
            if (M.compareTo(keys[2]) >= 0) {
                System.out.println("Error: Message must be less than n = " + keys[2]);
                return;
            }

            System.out.println("Original Message: " + M);

            // Encrypt the message
            BigInteger C = encrypt(M, keys[0], keys[2]);
            System.out.println("Encrypted Message: " + C);

            // Decrypt the message
            BigInteger decrypted = decrypt(C, keys[1], keys[2]);
            System.out.println("Decrypted Message: " + decrypted);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
