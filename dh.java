import java.util.Scanner;
class Main {
    // Modified power function to handle large numbers correctly
    private static long power(long a, long b, long p) {
        long result = 1;
        a = a % p;  // Update a if it is more than or equal to p
        
        while (b > 0) {
            // If b is odd, multiply result with a
            if ((b & 1) == 1)
                result = (result * a) % p;
            
            // Square a and divide b by 2
            a = (a * a) % p;
            b = b >> 1;  // b = b/2
        }
        return result;
    }

    // Function to check if a number is prime
    private static boolean isPrime(long n) {
        if (n <= 1) return false;
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Function to check if g is primitive root modulo p
    private static boolean isPrimitiveRoot(long g, long p) {
        long result = 1;
        for (int i = 1; i <= p-1; i++) {
            result = (result * g) % p;
            if (result == 1 && i < p-1) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long P, G, x, a, y, b, ka, kb;

        // Get P from user and validate
        while (true) {
            try {
                System.out.print("Enter a prime number P: ");
                P = scanner.nextLong();
                if (isPrime(P)) {
                    break;
                } else {
                    System.out.println("Error: P must be a prime number. Please try again.");
                }
            } catch (Exception e) {
                System.out.println("Please enter a valid number.");
                scanner.nextLine(); // Clear scanner buffer
            }
        }
        System.out.println("The value of P: " + P);

        // Get G from user and validate
        while (true) {
            try {
                System.out.print("Enter primitive root G (1 < G < P): ");
                G = scanner.nextLong();
                if (G > 1 && G < P && isPrimitiveRoot(G, P)) {
                    break;
                } else {
                    System.out.println("Error: G must be a primitive root modulo " + P + ". Please try again.");
                }
            } catch (Exception e) {
                System.out.println("Please enter a valid number.");
                scanner.nextLine(); // Clear scanner buffer
            }
        }
        System.out.println("The value of G: " + G);

        // Alice will choose the private key a
        System.out.print("Enter private key for Alice: ");
        a = scanner.nextLong();
        System.out.println("The private key a for Alice: " + a);
        
        // Gets the generated key
        x = power(G, a, P);
        
        // Bob will choose the private key b
        System.out.print("Enter private key for Bob: ");
        b = scanner.nextLong();
        System.out.println("The private key b for Bob: " + b);
        
        // Gets the generated key
        y = power(G, b, P);
        
        // Generating the secret key after the exchange of keys
        ka = power(y, a, P); // Secret key for Alice
        kb = power(x, b, P); // Secret key for Bob
        
        System.out.println("Secret key for Alice is: " + ka);
        System.out.println("Secret key for Bob is: " + kb);
        scanner.close();
    }
}
