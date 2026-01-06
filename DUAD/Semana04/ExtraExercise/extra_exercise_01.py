#1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    #1. Si el precio es menor a 100, el descuento es del 2%.
    #2. Si el precio es mayor o igual a 100, el descuento es del 10%.
    #3. *Ejemplos*:
        #1. 120 → 108
        #2. 40 → 39.2


discount = 0
final_price = 0

price_product = float(input("Enter price of the product: "))
if(price_product < 100):
    discount = price_product * 0.02
else:
    discount = price_product * 0.10

final_price = price_product - discount
print(f"The final price is: {final_price}")