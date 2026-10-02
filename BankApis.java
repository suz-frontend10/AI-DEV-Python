/**
 * Target interface expected by the client application (e.g., PhonePe).
 * Defines standard bank operations.
 */
public interface BankApis {
    void makeTransaction(String accountNo, int amount);
    int checkBalance(String accountNo);
}
