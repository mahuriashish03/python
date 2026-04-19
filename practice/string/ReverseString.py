def reverse_string(s):
    """
    Reverse the given string

    Args:
        s (str): Input string

    Returns:
        str: Reversed string
    """
    return s[::-1]

def reverse_string_using_for_loop(s):
    reversed_string = ""
    """
    Reverse the given string    
    :param s: Input String
    :return: Reversed String
    """
    for letter in s.split():
        reversed_String = letter + reversed_String

    return reversed_string

def main():
    # Input
    user_input = "hello"
    # Function call
    result = reverse_string(user_input)
    # Output
    print(f"Reversed string is: {result}")

    user_input = "Mahuri"
    result = reverse_string(user_input)
    print(f"Reversed String is: {result}")


if __name__ == "__main__":
    main()