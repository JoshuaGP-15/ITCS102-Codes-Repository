name = input('Enter Your Name --- ')
item = input('Enter Item Name --- ')

isFragile = bool(eval(input('Handle with care (True or False) --- ')))
distance = float(input('What is the distance? --- '))
weight = float(input('Weight of the item --- '))
is_express = bool(eval(input('As soon as possible? (True or False) --- ')))
is_international = bool(eval(input('International? (True or False) --- ')))

base_cost = (weight * 2.50) + (distance * 0.15)

free_shipping = weight <= 2 and distance <= 100 and is_express == False and is_international == False

if free_shipping:
    print('You got Free-shipping!!')
    total_cost = 0.00

elif is_international == True and is_express == True:
    total_cost = (base_cost * 1.40) + 50

elif is_express == True or (is_international == True and weight > 20):
    total_cost = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total_cost = base_cost + 30

else:
    total_cost = base_cost

#print
print('\n\t\t\t••• RECEIPT •••')
print('Sender Name ---', name)
print('Item ---', item)
print('Weight ---', weight)
print('Distance ---', distance)
print('Total Shipping Cost: $', total_cost)
