# An enhanced random number generator with error handling and multiple generation modes
import random

def validate_input(min_val, max_val, count):
    """
    Validate input parameters to ensure they meet our requirements.
    
    Args:
        min_val: The minimum value for random number generation
        max_val: The maximum value for random number generation
        count: How many numbers to generate
    
    Raises:
        ValueError: If any parameters are invalid
    """
    if not isinstance(min_val, int) or not isinstance(max_val, int):
        raise ValueError("Minimum and maximum values must be integers")
    
    if min_val >= max_val:
        raise ValueError("Minimum value must be less than maximum value")
    
    if not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer")

def generate_number(min_val=1, max_val=10, count=1):
    """
    Generate one or more random numbers between min_val and max_val.
    
    Args:
        min_val: The minimum value (inclusive), defaults to 1
        max_val: The maximum value (inclusive), defaults to 10
        count: How many numbers to generate, defaults to 1
    
    Returns:
        A list of random numbers if count > 1, or a single number if count = 1
    
    Raises:
        ValueError: If input parameters are invalid
    """
    try:
        validate_input(min_val, max_val, count)
        
        if count == 1:
            return random.randint(min_val, max_val)
        
        return [random.randint(min_val, max_val) for _ in range(count)]
    
    except ValueError as e:
        raise ValueError(f"Error generating numbers: {str(e)}")

def print_numbers(numbers, description=""):
    """
    Print the generated numbers in a friendly format.
    
    Args:
        numbers: A single number or list of numbers to print
        description: Optional description of the number set
    """
    if description:
        print(f"\n{description}")
    
    if isinstance(numbers, list):
        print("Generated numbers:")
        for i, num in enumerate(numbers, 1):
            print(f"Number {i}: {num}")
    else:
        print(f"Generated number: {numbers}")

def main():
    """
    Main function to demonstrate different number generation scenarios with error handling.
    """
    try:
        # Generate one number between 1 and 10
        print("\n--- Single Number (1-10) ---")
        single_number = generate_number()
        print_numbers(single_number, "Random number between 1 and 10:")
        
        # Generate 5 numbers between 1 and 35
        print("\n--- Multiple Numbers (1-35) ---")
        lottery_numbers = generate_number(1, 35, 5)
        print_numbers(lottery_numbers, "Five random numbers between 1 and 35:")
        
        # Demonstrate error handling with invalid input
        print("\n--- Error Handling Demo ---")
        try:
            invalid_numbers = generate_number(10, 5, 3)  # Invalid: min > max
        except ValueError as e:
            print(f"Caught error: {str(e)}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()