public class UPIPayment implements Payment, Refundable, Validatable {

    @Override
    public void processPayment(double amount) {
        System.out.println("Processing UPI payment of ₹" + amount);
    }

    @Override
    public void refundPayment(double amount) {
        System.out.println("Refunding UPI payment of ₹" + amount);
    }

    @Override
    public void validatePayment() {
        System.out.println("Validating UPI payment");
    }
}