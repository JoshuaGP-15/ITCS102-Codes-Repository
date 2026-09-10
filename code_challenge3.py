name = input('Enter Your Name --- ')
item = input('Enter Item Name --- ')

isFragile = bool(input('Handle with care --- '))
distance = float(input('What is the distance? --- '))
weight = float(input('Weight of the item --- '))
is_express = bool(input('As soon as possible? --- '))
is_international = bool(input('International? --- '))

base_cost = (weight * 2.50) + (distance * 0.15)

free_shipping = weight <= 2.0 or distance <= 100 and not is_express and not is_international

if free_shipping:
    total_cost = 0.00

elif is_international and is_express:
    total_cost = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total_cost = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total_cost = base_cost + 30

else:
    total_cost = base_cost

print('\n\t\t\t••• RECEIPT •••')
print('Sender Name ---', name)
print('Item ---', item)
print('Fragile ---', isFragile)
print('Weight ---', weight)
print('Distance ---', distance)
print('Express Delivery ---', is_express)
print('International Shipping ---', is_international)
print('Total Shipping Cost: $', total_cost)
