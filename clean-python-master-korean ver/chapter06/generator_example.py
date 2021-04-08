def multiple_generator(number, limit):
    counter = 1
    value = number * counter

    while value <= limit:
      yield value
      counter += 1
      value = number * counter

for num in multiple_generator(500, 5000):
    print(num)
