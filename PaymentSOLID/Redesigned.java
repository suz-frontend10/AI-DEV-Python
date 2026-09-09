public class Redesigned {

    public static void main(String[] args) {

        double amount = 1000;

        Payment payment = new CreditCardPayment();

        PaymentService paymentService = new PaymentService(payment);
        paymentService.makePayment(amount);

        Validatable validation = new CreditCardPayment();

        ValidationService validationService =
                new ValidationService(validation);
        validationService.validate();

        Refundable refund = new CreditCardPayment();

        RefundService refundService =
                new RefundService(refund);
        refundService.refund(amount);
    }
}