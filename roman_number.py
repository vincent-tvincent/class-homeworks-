import urllib
def roman_number_local(number):
    if int(number) <= 0:
        return Exception("please input a number greater than zero")
    roman_number = open("roman numerals.txt").readlines()
    return roman_number[int(number) - 1]


def roman_number_convert(number):
    #constants
    convert_list = [[1000, 'M'],[500, 'D'],[100, 'C'],[50, 'L'],[10, 'X'],[5, 'V'],[1, 'I']]

    #splitting the number
    digits = []
    for digit in convert_list:
        count = number // digit[0]
        digits.append([count,''])
        number -= digit[0] * count

    #converting to roman number
    index_list = range(len(digits))
    for i in index_list:
        if i > 0 and (convert_list[i-1][0] - digits[i][0] * convert_list[i][0] == convert_list[i][0]): #judge if the number is special number like 4, 9, 40...
            digits[i-1][1] += convert_list[i][1] + convert_list[i-1][1]
        else:
            repeating_times = range(digits[i][0])
            for digit in repeating_times:
                digits[i][1] += convert_list[i][1]

    #assemble every part together
    result = ''
    for digit in digits:
        result += digit[1]
    print('converting completed: ',result)
    return result

number = roman_number_convert()










