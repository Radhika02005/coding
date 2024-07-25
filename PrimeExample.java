import java.util.Scanner;

public class PrimeExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = scanner.nextInt();  // Read user input
        boolean isPrime = true;  // Flag to indicate if the number is prime

        // Check if the number is less than 2, which are not prime numbers
        if (number < 2) {
            System.out.println(number + " is not a prime number");
        } else {
            // Loop from 2 to the square root of the number
            for (int i = 2; i <= number / 2; i++) {
                if (number % i == 0) {
                    System.out.println(number + " is not a prime number");
                    isPrime = false;
                    break;
                }
            }

            // If the number is still considered prime, print the result
            if (isPrime) {
                System.out.println(number + " is a prime number");
            }
        }

        scanner.close();
    }
}
