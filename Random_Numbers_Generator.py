#======Random Numbers Generator ======

from random import shuffle

lottery = list(range(1, 40))
numbers = []

print ("Random Lottery Numbers")
for i in range(6):
    shuffle(lottery)
    x = lottery.pop()
    numbers.append(x)

numbers.sort()
print ("This might be your lucky day! Your numbers are:", numbers)
