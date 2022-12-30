#4.3
# for value in range(1, 21):
#     print(value)
# 4.4
# for value in range(1, 1_0000_001):
#     print(value)
# 4.5
# numbers = []
#
# for value in range(1, 1_0000_001):
#     numbers.append(value)
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# 4.6
# for value in range(1, 21, 2):
#     print(value)
# 4.7
# numbers = [value for value in range(3, 31, 3)]
# for number in numbers:
#     print(number)
# 4.8 and 4.9
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)