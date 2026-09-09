//BRUTE FORCE

import java.util.Scanner;

class BruteForcePayment {

    public void processPayment(String paymentType, double amount) {

        if (paymentType.equalsIgnoreCase("Credit Card")) {

            System.out.println("Processing Credit Card payment of ₹" + amount);

        } else if (paymentType.equalsIgnoreCase("UPI")) {

            System.out.println("Processing UPI payment of ₹" + amount);

        } else if (paymentType.equalsIgnoreCase("Cash")) {

            System.out.println("Processing Cash payment of ₹" + amount);

        } else {

            System.out.println("Invalid payment type");

        }

    }

    public void refundPayment(String paymentType, double amount) {

        if (paymentType.equalsIgnoreCase("Credit Card")) {

            System.out.println("Refunding Credit Card payment of ₹" + amount);

        } else if (paymentType.equalsIgnoreCase("UPI")) {

            System.out.println("Refunding UPI payment of ₹" + amount);

        } else if (paymentType.equalsIgnoreCase("Cash")) {

            System.out.println("Refunding Cash payment of ₹" + amount);

        } else {

            System.out.println("Invalid payment type");

        }

    }

    public void validatePayment(String paymentType) {

        if (paymentType.equalsIgnoreCase("Credit Card")) {

            System.out.println("Validating Credit Card payment");

        } else if (paymentType.equalsIgnoreCase("UPI")) {

            System.out.println("Validating UPI payment");

        } else if (paymentType.equalsIgnoreCase("Cash")) {

            System.out.println("Validating Cash payment");

        } else {

            System.out.println("Invalid payment type");

        }

    }

}

/*
 * 1)SRP processPayment(), refundPayment(), and validatePayment() are
 * different responsibilities in a signle class "processPayment"
 */

/*
 * 2)OCP What happens if we add PayPal to payment type , we have to modify the
 * existing class larger, harder to maintain,
 * and every new payment type requires modifying existing code in multiple
 * functions.
 * Adding or changing a payment method should not require continuously modifying
 * one large Payment class
 */

/*
 * 3) If Cash doesn't support refunds,
 * but our design gives every payment type a refundPayment() operation,
 * Can a child/subtype be used wherever the parent type is expected without
 * causing incorrect behavior?
 */

/*
 * 4)The child (CashPayment) cannot properly behave like the parent (Payment)
 * because the parent promises behavior that the child cannot fulfill.
 */

// ISP = Interface Segregation Principle Don't force a class to depend
// on methods that it doesn't need or cannot support.
// Card → can pay + refund
// UPI → can pay + refund
// Cash → can pay but cannot refund through the same mechanism

public class Bruteforce {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        BruteForcePayment payment = new BruteForcePayment();

        System.out.print("Enter payment type: ");

        String paymentType = sc.nextLine();

        System.out.print("Enter amount: ");

        double amount = sc.nextDouble();

        System.out.println("\n--- Payment Validation ---");

        payment.validatePayment(paymentType);

        System.out.println("\n--- Processing Payment ---");

        payment.processPayment(paymentType, amount);

        System.out.println("\n--- Refund ---");

        payment.refundPayment(paymentType, amount);

        sc.close();

    }

}

// DIP says: Don't depend on the concrete payment type.

/*
 * class PaymentService {
 * private Payment payment;
 * 
 * PaymentService(Payment payment) {
 * this.payment = payment;
 * }
 * 
 * void makePayment() {
 * payment.pay();
 * }
 * }
 */

/*
 * Our normal payment service can depend on:Payment
 * because all payment types can pay, But a refund service should depend
 * on:Refundable not Payment.
 */

/*
 * | Principle | Simple meaning | Payment scenario |
 * | --------------------------------------- |
 * -----------------------------------------------------------------------------*
 * --- |
 * -----------------------------------------------------------------------------*
 * ----------------------------------------------------- |
 * | **S — Single Responsibility Principle** | One class should have **one main
 * responsibility**. | `Payment` handles `processPayment()`, `refundPayment()`,
 * and `validatePayment()` → too many responsibilities. |
 * | **O — Open/Closed Principle** | **Open for extension, closed for
 * modification.** | Adding `PayPal` shouldn't require adding another `else if`
 * inside the existing `Payment` class. |
 * | **L — Liskov Substitution Principle** | A child should be safely usable
 * wherever its parent is expected. | If `Payment` promises `refund()`, but
 * `CashPayment` cannot properly refund, `CashPayment` cannot safely substitute
 * that `Payment`. |
 * | **I — Interface Segregation Principle** | Don't force a class to implement
 * methods it doesn't need. | Don't force `CashPayment` to implement
 * `refundPayment()` just because other payment types support it. |
 * | **D — Dependency Inversion Principle** | High-level code should depend on
 * **abstractions**, not concrete implementations. | `PaymentService` should
 * depend on `Payment`, not directly on `CreditCardPayment` or `UPIPayment`. |
 */