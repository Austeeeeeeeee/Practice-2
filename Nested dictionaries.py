print('---------------------------------------------------------------NESTED DICTIONARIES------------------------------------------------------------------')
nested_dictionary = {
 'New York': {'continent':'North America','population': 12},
 'New Delhi' : {'continent': "Asia", 'population': 23},
 'Tanzania'  : {'continent' : 'Africa', 'population': 67},
 'Columbia'  : {'continent' : 'South America','population': 89}
}

print('-----------------------------------------------------------------------------------------')
print('POP METHOD')
print('--Removing a key of top level')
nested_dictionary.pop('New Delhi')
print(nested_dictionary)

print('--Removing a key in a nested dictionary.')
nested_dictionary['New York'].pop('population')
print(nested_dictionary)


print('-----------------------------------------------------------------------------------------')
print('DEL METHOD')
print('--Removing a key in a nested dictionary.')
del nested_dictionary['Tanzania']['population']
print(nested_dictionary)

print('-----------------------------------------------------------------------------------------')
print('UPDATE TOP LEVEL KEY - KEEP VALUE')
i = {
 'Jonas': {'surname': 'gii', 'age': 67}
}

i['Roman'] = i.pop('Jonas')
print(i)


print('-----------------------------------------------------------------------------------------')
print('UPDATE TOP LEVEL KEY - KEEP VALUE')
i = {
 'Jonas': {'surname': 'Gringg', 'age': 67}
}

i['Jonas']['Country'] = 'Lithuania'
print(i)

print('-----------------------------------------------------------------------------------------')
print('CHANGE VALUE OF INNER DICTIONARY')
ii = {
 'Jonas': {'surname': 'Gringg', 'age': 67}
}

ii['Jonas']['surname'] = 'Petrasautis'
print(ii)

print('-----------------------------------------------------------------------------------------')
print('CHANGE KEY OF INNER DICTIONARY')
iii = {
 'Jonas': {'surname': 'Gringg', 'age': 67}
}

iii['SURNAME'] = iii['Jonas'].pop('surname')
print(iii)


print('')
print('')
print('')
print('-----------------------------------------------------------------------------------------')
print('ADDING COMPLETE DICTIONARY')
dictio = {
 'Tanzania'  : {'continent' : 'Africa', 'population': 67},
 'Columbia'  : {'continent' : 'South America','population': 89}
}

dictio['London'] = {'continent': 'Europe', 'population': 33}
print(dictio)






print('-----------------------------------------------------------------------------------------')
print('PRINTING THE DICTIONARY')
print(nested_dictionary.items())
print(nested_dictionary['Tanzania'].items())
print(nested_dictionary['Tanzania'].keys())

print('')
print('Looping through the items')
for k,v in nested_dictionary['Tanzania'].items():
 print(k,':',v)


print('')
for key in nested_dictionary.keys():
 print(f'This is the key {key}')


print('')
print('DICTIONARY CONVERTION')
print('Converting the dictionary into the list and printing by index')
dic_list = list(nested_dictionary.items())
print(dic_list)
#print(dic_list[1])



print('')
print('her')
nested_dictionary['Senegal'] = nested_dictionary['Tanzania']
print(nested_dictionary)



print('-----------------------------------------------------------------------------------------')
nested_dictionary.pop('New York')
print(nested_dictionary)