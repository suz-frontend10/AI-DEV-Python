/**
 * Adapter class that implements the target interface `BankApis`
 * and wraps an instance of `IciciBankApi` (Adaptee).
 * 
 * Translates client calls:
 * - `makeTransaction()` -> `iciciBankApi.sendMoney()`
 * - `checkBalance()` -> `iciciBankApi.fetchBalance()`
 */
public class IciciBankAdapter implements BankApis {

    private final IciciBankApi iciciBankApi;

    public IciciBankAdapter() {
        this.iciciBankApi = new IciciBankApi();
    }

    public IciciBankAdapter(IciciBankApi iciciBankApi) {
        this.iciciBankApi = iciciBankApi;
    }

    @Override
    public void makeTransaction(String accountNo, int amount) {
        // Translate call to ICICI Bank's sendMoney method
        iciciBankApi.sendMoney(accountNo, amount);
    }

    @Override
    public int checkBalance(String accountNo) {
        // Translate call to ICICI Bank's fetchBalance method
        return iciciBankApi.fetchBalance(accountNo);
    }
}
