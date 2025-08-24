def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    print("The final price is: ", final_price)
