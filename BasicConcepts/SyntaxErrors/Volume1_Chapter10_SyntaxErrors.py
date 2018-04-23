# While loop syntax errors.
while False
    print("In body of while loop!")

example_number = 2
while example_number < 5:
print("In body of while loop!")
example_number = example_number + 1

while example_number < 10:
        print("In body of while loop!")
      print("Here's another line!")
    print(example_number)
    example_number += 1

while example_number < 15:
    example_number_is_even = example_number % 2 == 0
    if example_number_is_even:
            break

        example_number += 1

# For loop syntax errors.
for iteration range(5):
    print(iteration)

for iteration in range(5)
    print(iteration)

for iteration in range(5):
        print(iteration)

for iteration in range(5):
  print(iteration)
    print(iteration * 2)

for iteration in range(2 10):
    print(iteration)

for iteration in range(2; 10):
    print(iteration)

for iteration in range(5, 10):
    print(iteration)
        if True:
        print("Printing after iteration!")
        else:
            break
