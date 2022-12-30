pizzas = ["Pepperoni", "Margaret", "Hawaiian"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love pizza!")

# 4.11
friend_pizzas = pizzas[:]
friend_pizzas.append("Carbonara")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)