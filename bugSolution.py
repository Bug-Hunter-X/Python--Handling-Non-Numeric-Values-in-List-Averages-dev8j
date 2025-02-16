def calculate_average(numbers):
    try:
        if not numbers:
            return 0  # Handle empty list
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List contains non-numeric values.")
        return None #or raise a more descriptive exception 

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_strings = [1,2,'a',4]
result = calculate_average(my_list_with_strings) #This will print an error message now