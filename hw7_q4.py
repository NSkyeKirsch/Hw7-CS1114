import super_secret_module

def is_impostor(information, corrupter_function):
    # find out if the list is deep or shallow (True if deep)
    # information is original list

    information.insert(0, ['a', 'b', 'c'])

    corrupted_str = corrupter_function(information)

    information[0][1] = 2

    print(information)
    print(corrupted_str)

    if information[0][1] != corrupted_str[0][1]:
        return True
    else:
        return False


def main():
    original_list = [1, 2, 3]

    print(is_impostor(original_list, super_secret_module.corrupter))

main()