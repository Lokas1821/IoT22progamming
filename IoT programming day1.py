# write all between 1 and 100

for number in range(1, 101, 1):
    
    if number == 42:
        print("Answer to the Ultimate Question of Life, the Universe, and Everything")
    elif number % 3 == 0:
       print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")
    
