def order(burger, location = 'Mohakhali'):
    price = 0
    if burger == 'BBQ Chicken Cheese Burger':
        price += 250
    elif burger == 'Beef Burger':
        price += 170
    elif burger == 'Naga Drums':
        price += 200
    price = (price * 0.08 + price) 
    if location == 'Mohakhali':
        price += 40
    else:
        price += 60
    return price

print(order('Beef Burger','Dhanmondi') )

print(order('Beef Burger'))

