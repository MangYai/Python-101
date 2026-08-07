numbers = [4, 2, 9, 1, 5, 6]
length = len(numbers)
print(f"lenght of the list: {length}")

total_sum = sum(numbers)
print(f"Sum of all element: {total_sum}")

max_value = max(numbers)
print(f"Minimun value: {max_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [False, True, False]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_true = all(bool_list)
print(f"Are all element True? {all_true}")

string = "hello"
char_list = list(string)
print(f"List of characters: {char_list}")

reversed_numbers = list(reversed(numbers))
print(f"reversed list: {reversed_numbers}")

enumerate_number = list(enumerate(numbers))
print(f"Enumenrate list: {enumerate_number}")