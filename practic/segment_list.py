segments = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print("The irst three items in the list are:")
# for segment in segments[0:3]:
#     print(segment)

print("Three items from the middle of the list are:")
for segment in segments[2:5]:
    print(segment)

print("The last three items in the list are:")
for segment in segments[-3:]:
    print(segment)