cart = {
    "alma": (1.5, 6),
    "corek": (0.8, 2),
    "sud": (2.2, 1)
}
def calculate_total(cart,discount_limit = 10):
    total = 0
    for product , (price,quantity) in cart.items():
        total += price*quantity
    if total >= discount_limit:
        discount = total*0.9
    else:
        discount = total

    return discount,total
total, discount = calculate_total(cart)
for product, (price, quantity) in cart.items():
    print(f"{product:<10} {quantity} x {price} = {price * quantity}")
print(f"Cəmi: {total} AZN")
print(f"Endirimli: {discount} AZN")