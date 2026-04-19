def is_palindrome(s):
    """
    :Input param: Input String
    :return: True if palindrome else False
    """
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def main():

    user_input = "aba"
    result = is_palindrome(user_input)
    print(f"String is palindrome: {result}")

if __name__ =="__main__":
    main()