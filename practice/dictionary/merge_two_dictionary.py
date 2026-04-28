def merge_dictionary(dics1 , dics2):
    # This will overwirte the values of matching key. Here the key value from dics2 will be replaced
    # return {**dics1, **dics2}
    return dics1 | dics2

def merge_two_dictionary(dics1 , dics2):
    result = dics1.copy()
    # The matching key values will be added.
    for key, value in dics2.items():
        result[key] = result.get(key, 0) + value

    return result

def main():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print(merge_dictionary(d1, d2))
    print(merge_two_dictionary(d1, d2))

if __name__ == "__main__":
    main()