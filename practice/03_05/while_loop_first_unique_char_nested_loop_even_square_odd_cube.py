def print_number():
    number = 10
    while number > 0:
        print(number)
        number -=1

def first_unique_char(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    for letter in string:
        if frequency[letter] == 1:
            return letter
    return ""

def print_pattern(number):
    for i in range(number):
        for j in range(number):
            if j<=i:
                print("*", end="")
        print()

def square_cube(number):
    if number%2 == 0:
        return number**2
    else:
        return number**3


def main():
    print_number()
    print(first_unique_char("madam"))
    print_pattern(3)
    print(square_cube(3))


if __name__ == "__main__":
    main()