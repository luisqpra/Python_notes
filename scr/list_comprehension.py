# Generate a list of numbers in a single line of code
numbers_list = [number for number in range(1, 16)]
numbers_odd_list = [num_odd for num_odd in range(1, 16) if num_odd % 2]

if __name__ == "__main__":
    print("numbers between 1 to 15\n\t", numbers_list)
    print("odd numbers between 1 to 15\n\t", numbers_odd_list)
