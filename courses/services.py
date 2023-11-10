from config.settings import STRIPE_SECRET_KEY
import stripe


def get_a_link_to_pay_for_the_course(course):

    stripe.api_key = STRIPE_SECRET_KEY

    product = stripe.Product.create(name=course.title)

    price = stripe.Price.create(
        unit_amount=course.price,
        currency="usd",
        recurring={"interval": "month"},
        product=product.id,
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
    )

    return payment_link.url
