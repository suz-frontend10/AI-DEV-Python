public class ValidationService {

    private Validatable payment;

    public ValidationService(Validatable payment) {
        this.payment = payment;
    }

    public void validate() {
        payment.validatePayment();
    }
}