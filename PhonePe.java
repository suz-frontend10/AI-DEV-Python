/**
 * PhonePe client application context that depends on `BankApis` interface.
 * Uses Dependency Injection so any bank adapter (ICICI, HDFC, SBI, etc.) can be used.
 */
public class PhonePe {

    private final BankApis bankApis;

    public PhonePe() {
        // Default adapter
        this.bankApis = new IciciBankAdapter();
    }

    public PhonePe(BankApis bankApis) {
        this.bankApis = bankApis;
    }

    public void makeTransaction(String accountNo, int amount) {
        bankApis.makeTransaction(accountNo, amount);
    }

    public int checkBalance(String accountNo) {
        return bankApis.checkBalance(accountNo);
    }
}
