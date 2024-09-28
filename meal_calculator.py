

meal_price = float(input('Input meal price in dollars and cents: (i.e. 13.68)'))

tip = meal_price * 0.18
tax = meal_price * 0.07

print('18% tip: {:.2f}'.format(tip))
print('7% tax: {:.2f}'.format(tax))
print('Meal Price + tax with tip: {:.2f}'.format(meal_price + tax + tip))