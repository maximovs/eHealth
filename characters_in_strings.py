# Some considerations:
# I asume that character means any ASCII character. Otherwise, I would filter in the corresponding subgroup.
# I asume that characters should only be returned once, that's why I check if it's already in result.


def characters_in_string_order_n(string_1, string_2):
    chars_in_string_2 = list()
    for char in string_2:
        if char not in chars_in_string_2:
            chars_in_string_2.append(char)

    result = list()

    for char in string_1:
        if char in chars_in_string_2 and char not in result:
            result.append(char)

    return result


def characters_in_string_order_nxn(string_1, string_2):
    result = list()
    for char in string_1:
        if char in string_2 and char not in result:
            result.append(char)

    return result

string_1 = "Hello, how are you?" * 1000
string_2 = "Hi, what's up?" * 1000
print characters_in_string_order_n(string_1, string_2)
print characters_in_string_order_nxn(string_1, string_2)