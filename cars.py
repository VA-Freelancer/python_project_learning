cars = ['audi', 'bmw', 'toyota', 'subaru']
# cars.sort() сортировка по порядку, изменяет искходный массив
# print(cars)
# cars.sort(reverse=True) обратный порядок сортировки
# print(cars)

# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars)) # не изменяет исходный массив
# print("Here is the original list again:")
# print(cars)
#
# cars.reverse()
# print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())