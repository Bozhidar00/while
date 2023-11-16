def read_numbers():
    target_sum = int(input("Enter a whole number: "))
    current_sum = 0
    numbers = []

    while current_sum < target_sum:
        num = int(input())
        numbers.append(num)
        current_sum += num

    print("The sum is:", sum(numbers))

read_numbers()
