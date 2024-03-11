def calculate_discount(price,discount_percent):
    if discount_percent >=20:
        discount_amount=price*(discount_percent/100)
        final_price=price-discount_amount
        return final_price
    else:
        return price
price=float(input("enter price:")) 
discount_percent=float(input("enter discount_percent:"))
final_price=calculate_discount(price,discount_percent)
if final_price==price:
        print("no discount applied:",final_price)
else:
         print("Final price after applying discount:",final_price)


    

