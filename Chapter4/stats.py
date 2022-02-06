#Chapter 4 Hands on #2 Russell Arlt
import random

ran_num = random.randrange(10,100)

print(f"Random number chosen is {ran_num}")
num_list = [value for value in range(0,ran_num + 1)]
print(num_list)
print(f"The largest number {max(num_list)}")
print(f"The smallest number {min(num_list)}")
x_num = 0
for x in num_list:
    x_num = x_num + x
print(f"The total of all the numbers = {x_num}")

avg_num = x_num / max(num_list)
print(f"The average number = {avg_num}")




