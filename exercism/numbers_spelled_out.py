def solution():
    unity_values = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    ten_to_nineteen = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    decimal_values = {
        2: "twenty",
        3: "thirty",
        4: "fourty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    numbers_and_names = {}
    for number in range(0, 100):
        if number < 10:
            numbers_and_names[number] = unity_values[number]
        elif number >= 10 and number < 20:
            numbers_and_names[number] = ten_to_nineteen[int(str(number)[1])]
        elif number >= 20:
            if str(number)[1] == "0":
                numbers_and_names[number] = decimal_values[int(str(number)[0])]
            else:
                numbers_and_names[number] = (
                    f"{decimal_values[int(str(number)[0])]}-{unity_values[int(str(number)[1])]}"
                )

    return numbers_and_names


print(*solution().items(), sep="\n")
