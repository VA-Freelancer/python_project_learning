guests = ['Alexandr', 'Mihail', 'Ilia']
#
for guest in guests:
    print(f"\n {guest.title()} приглашаю тебя на день рождения")

not_guest = "Mihail"
change_guest = "Sergei"
# заменяем гостя
guests.remove(not_guest)
guests.append(change_guest)
print(f"\n {not_guest.title()} не сможет придти")
#
for guest in guests:
    print(f"\n {guest.title()} приглашаю тебя на день рождения")

print(f"Список приглашенных увеличиться так как, привезут новый обеденный стол")
middle_length_list_guests = int(len(guests) / 2)
guests.insert(0, 'Tatiana')
guests.insert(middle_length_list_guests, 'Vladimir')
guests.append('Olga')
# 3.9
print(len(guests))
for guest in guests:
    print(f"\n {guest.title()} приглашаю тебя на день рождения")

print(f"Список приглашенных уменьшится  так как, новый обеденный стол задерживается")
list_exclude = ['Tatiana', 'Vladimir', 'Ilia', 'Olga']

for el in list_exclude:
    guests.remove(el)
    print(f"\n {el.title()}, я сожалею об отмене приглашения")

print(len(guests))

for guest in guests:
    print(f"\n {guest.title()}, приглашение остается в силе")

del guests[0:2]

print(guests)
