public class WalletPayment implements Payment, Refundable, Validatable {

    @Override
    public void processPayment(double amount) {
        System.out.println("Processing Wallet payment of ₹" + amount);
    }

    @Override
    public void refundPayment(double amount) {
        System.out.println("Refunding Wallet payment of ₹" + amount);
    }

    @Override
    public void validatePayment() {
        System.out.println("Validating Wallet payment");
    }
}