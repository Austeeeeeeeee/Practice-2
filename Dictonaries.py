print('---------------------------------------------------------------NESTED DICTIONARIES------------------------------------------------------------------')
print('Printing keys and values')
cities = {'North America': 'New York','South America': 'Peru','Europe':'Paris','Asia': 'Singapur','Africa':'Tanzania'}
print(cities.values())
print(cities.keys())



print('-----------------------------------------------------------------------------------------')
print('POP METHOD - return value')
print('Removing key of a top level')
popped_items = cities.pop('North America')
print(cities)
print(f'These are the popped items, returning it\'s value "{popped_items}"')



print('-----------------------------------------------------------------------------------------')
print('DEL METHOD - No value return')
del cities['South America']
print(cities)



print('-----------------------------------------------------------------------------------------')
print('DELETES LAST ITEM')
cities.popitem()
print(cities)


print('-----------------------------------------------------------------------------------------')
print('GET METHOD - get value of a key')
get = cities.get('Africa')
print(get)


print('-----------------------------------------------------------------------------------------')
print('GET METHOD - Non existing key -> returns None')
print(cities.get('Australia'))



print('-----------------------------------------------------------------------------------------')
print('GET METHOD - Non existing key -> set default')
print(cities.get('Australia','Sidney'))
print(cities)


print('-----------------------------------------------------------------------------------------')
print('FROMKEYS METHOD')
print('Creates values for the provided keys')
print('It can be used with list,tuples,set,string or range')
d = dict.fromkeys(range(10),'value')
print(d)
print(d.pop(4))
print(d)


print('-----------------------------------------------------------------------------------------')
print('UPDATE METHOD')
print(d | {10:'valuee'})
print('')


print('-----------------------------------------------------------------------------------------')
print('ADD KEY/DUPLICATE VALUE')
('Keeps the old key + add new key duplicating the value of the old key into the new one'
 'two keys named after Asia sharing the same value')
cities['REMOVED_KEY'] = cities['Asia']
print(cities)

print('-----------------------------------------------------------------------------------------')
print('RENAME KEY AND REMOVE THE OLD ONE')
cities['ASIA2'] = cities.pop('Asia')
print(cities)









'''
def info():
	name = input('Enter you name: ')
	age = int(input('Enter your age: '))
	nationality = input('Enter your nationality: ')
	return{
	'Name':name,
	'Age':age,
	'Nationality':nationality
}
dic = info()
print(dic)
'''
print('')
print('')
dicta = {}
dicta['Name'] = 'Mario'
print(dicta)
dicta['Name'] = 'Mari'
print(dicta)