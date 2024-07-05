# Словарь
my_dict = {'Pavel':1970, 'Rimma':1991, 'Mikl':1995, 'Oleg':2002}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Rimma'])
print('Not existing value: ', my_dict.get('Serg'))
my_dict.update({'Vlad':2000, 'Lena':1983})
c = my_dict.pop('Oleg')
print('Deleted value: ', c)
print('Modified dictionary: ', my_dict)
# Множество
my_set = {9.81, 'Rock', 2, 'Rock', 11, 2}
print('Set: ', my_set)
my_set.add(-3.14)
my_set.add('Pear')
my_set.discard(11)
print('Modified set: ', my_set)

