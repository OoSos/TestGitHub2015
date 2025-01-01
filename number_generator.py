# A simple random number generator to demonstrate Git version control
import random

def generate_number(min_val=1, max_val=10, count=1):
    """
    Generate one or more random numbers between min_val and max_val.
    
    Parameters:
        min_val: The minimum value (inclusive), defaults to 1
        max_val: The maximum value (inclusive), defaults to 10
        count: How many numbers to generate, defaults to 1
    
    Returns:
        A list of random numbers if count > 1, or a single number if count = 1
    """
    if count == 1:
        return random.randint(min_val, max_val)
    
    return [random.randint(min_val, max_val) for _ in range(count)]

def print_numbers(numbers):
    """
    Print the generated numbers in a friendly format.
    """
    if isinstance(numbers, list):
        print("Your random numbers are:")
        for i, num in enumerate(numbers, 1):
            print(f"Number {i}: {num}")
    else:
        print(f"Your random number is: {numbers}")

if __name__ == "__main__":
    # Generate one number
    single_number = generate_number()
    print_numbers(single_number)
    
    print("\n" + "-"*30 + "\n")  # Separator for clarity
    
    # Generate multiple numbers
    multiple_numbers = generate_number(count=5)
    print_numbers(multiple_numbers)