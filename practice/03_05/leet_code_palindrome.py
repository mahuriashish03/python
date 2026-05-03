def is_palindrome(s):
    if not s:
        return True
    clean_value  = []
    for char in s:
        if char.isalnum():
            clean_value.append(char.lower())

    clean_value = "".join(clean_value)

    return clean_value == clean_value[::-1]
