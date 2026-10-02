/**
 * Entry point / Test runner for Adapter Design Pattern demonstration.
 */
public class Client {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("   ADAPTER DESIGN PATTERN DEMO - PhonePe & ICICI  ");
        System.out.println("==================================================\n");

        // Instantiating PhonePe with default ICICI Bank Adapter
        PhonePe phonePe = new PhonePe();

        System.out.println("1. Performing Transaction...");
        phonePe.makeTransaction("ACC-987654321", 600);

        System.out.println("\n2. Checking Account Balance...");
        int balance = phonePe.checkBalance("ACC-987654321");
        System.out.println("Available Balance: $" + balance);

        System.out.println("\n==================================================");
        System.out.println("   DEMO COMPLETED SUCCESSFULLY                    ");
        System.out.println("==================================================");
    }
}
