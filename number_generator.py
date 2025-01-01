# A simple random number generator to demonstrate Git version control
import random

def generate_number(min_val=1, max_val=100):
    """Generate a random number between min_val and max_val."""
    return random.randint(min_val, max_val)

if __name__ == "__main__":
    print(f"Your random number is: {generate_number()}")