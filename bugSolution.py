def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 0] 
result = calculate_average(my_numbers) 
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

#my_numbers = [10,20,30,'a']
#result = calculate_average(my_numbers) #this will raise an error
#print(f"The average is: {result}") 