motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# add element to list in end
# motorcycles.append('ducati')
# print(motorcycles)
# add in the specified
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# delete element in list
# del motorcycles[0]
# del motorcycles[1]
# print(motorcycles)
# last_owned = motorcycles.pop() удаляет произвольное значение
# print(motorcycles)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# last_owned = motorcycles.pop(0) удаляет по индексу сохроняет значение после
# print(motorcycles)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# motorcycles.remove('ducati') ищет и удаляет элемент по значению
# print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n {too_expensive.title()} is too expensive for me")
print(motorcycles[-1])