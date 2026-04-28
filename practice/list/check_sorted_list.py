def check_sorted_list(my_list):
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            return False
    return True

def main():
    my_list = list(map(int, input("Input your values: ").split()))
    print(check_sorted_list(my_list))

if __name__ == "__main__":
    main()
