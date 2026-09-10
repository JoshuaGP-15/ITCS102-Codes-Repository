name = input('Enter Your Name ---')
item = input('Enter Item Name ---')


isFragile = bool(input('Handle with care ---'))
distance = float(input('What is the distance? ---'))
weight = float(input('Weight of the item ---'))
is_express = bool(input('As soon as possible --- ?'))
is_international = bool(input('International'))


#calculations
#Total Cost
base_cost = (weight * 2.50) + (distance * 0.15)	

# free shipping
free_shipping = ( weight <= 2.0 and distance <= 100)





print('total cost', base_cost)
print('you got a free shipping!', free_shipping) 
