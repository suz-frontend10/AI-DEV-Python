/**
 * Adaptee class representing ICICI Bank's legacy or third-party API.
 * This class has incompatible method names (`sendMoney` and `fetchBalance`) 
 * relative to the target `BankApis` interface.
 */
public class IciciBankApi {
    
    public void sendMoney(String accountNo, int amount) {
        System.out.println("Processing transaction via ICICI Bank API...");
        System.out.println("  Account Number: " + accountNo);
        System.out.println("  Amount: $" + amount);
        System.out.println("Transaction status: SUCCESS");
    }

    public int fetchBalance(String accountNo) {
        System.out.println("Fetching balance from ICICI Bank API for account: " + accountNo);
        return 5000;
    }
}
