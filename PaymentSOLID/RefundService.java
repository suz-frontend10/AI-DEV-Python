public class RefundService {

    private Refundable payment;

    public RefundService(Refundable payment) {
        this.payment = payment;
    }

    public void refund(double amount) {
        payment.refundPayment(amount);
    }
}