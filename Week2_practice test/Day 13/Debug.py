def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)):
        total += int(numbers[i])

    return total / len(numbers)


numbers = input("Enter numbers separated by commas: ")
numbers = numbers.split(",")

average = calculate_average(numbers)

print("Average:", average)
