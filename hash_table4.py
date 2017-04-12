input_string = "1, 23, 4,55, 66, 56,   77, 45, 67, 103,   75,3"
highest_value = 0

split_values = input_string.split(',')
# print arr

for number_string in split_values:
    if len(number_string) != 0:
        number = int(number_string.strip())
        if highest_value < number:
            highest_value = number

print highest_value
