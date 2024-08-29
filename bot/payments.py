import paypalrestsdk
import razorpay
from bot.config import PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET, RAZORPAY_API_KEY, RAZORPAY_API_SECRET

# Initialize PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # Or "live" for production
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})

# Initialize Razorpay Client
razorpay_client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))

def create_paypal_payment(amount, currency="USD"):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [{
            "amount": {"total": str(amount), "currency": currency},
            "description": "Payment for 1080p video access"
        }],
        "redirect_urls": {
            "return_url": "https://your-redirect-url.com/execute",
            "cancel_url": "https://your-redirect-url.com/cancel"
        }
    })
    if payment.create():
        return payment
    else:
        return None

def create_razorpay_payment(amount, currency="INR", payment_method="upi"):
    order = razorpay_client.order.create({
        "amount": int(amount * 100),  # Amount in paise
        "currency": currency,
        "payment_capture": "1"
    })
    return order

def verify_razorpay_payment(payment_id, signature, order_id):
    try:
        razorpay_client.utility.verify_payment_signature({
            'razorpay_payment_id': payment_id,
            'razorpay_order_id': order_id,
            'razorpay_signature': signature
        })
        return True
    except:
        return False
