
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()


"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = # Your code here
    odd_numbers = # Your code here
    
    # Calculate average
    average = # Your code here
    
    # Numbers greater than average
    above_average = # Your code here
    
    # Display results
    # Your code here


def number_operations():
    numbers = []
    
   # Display original list
    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input(f"Number {i+1}: "))
        numbers.append(num)
    
     # Create filtered lists
    print(f"\nOriginal numbers: {numbers}")
    
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = [num for num in numbers if num > average]
    
   
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than average ({average:.2f}): {above_average}")
    
   
    print("\nStatistics:")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {average:.2f}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")

if __name__ == "__main__":
    number_operations()
