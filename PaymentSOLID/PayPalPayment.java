public class PayPalPayment implements Payment, Refundable, Validatable {

    @Override
    public void processPayment(double amount) {
        System.out.println("Processing PayPal payment of ₹" + amount);
    }

    @Override
    public void refundPayment(double amount) {
        System.out.println("Refunding PayPal payment of ₹" + amount);
    }

    @Override
    public void validatePayment() {
        System.out.println("Validating PayPal payment");
    }
}