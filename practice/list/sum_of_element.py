def sum_of_elements(my_list):
    sum = 0
    for element in my_list:
        sum += element
    return sum

def main():
    my_list = list(map(int, input("Inter the numbers").split()))
    print(sum_of_elements(my_list))

if __name__ == "__main__":
    main()