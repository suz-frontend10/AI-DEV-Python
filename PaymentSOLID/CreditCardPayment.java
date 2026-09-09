public class CreditCardPayment implements Payment, Refundable, Validatable {

    @Override
    public void processPayment(double amount) {
        System.out.println("Processing Credit Card payment of ₹" + amount);
    }

    @Override
    public void refundPayment(double amount) {
        System.out.println("Refunding Credit Card payment of ₹" + amount);
    }

    @Override
    public void validatePayment() {
        System.out.println("Validating Credit Card payment");
    }
}