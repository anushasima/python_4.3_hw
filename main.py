import random

elements = random.randint(3, 10)
random_list = [random.randint(1, 100) for _ in range(elements)]
print(random_list)
new_list = [random_list[0], random_list[2], random_list[-2]]
print(new_list)

# my_list = [1, 2, 3, 4, 5, 6, 7, 9]


