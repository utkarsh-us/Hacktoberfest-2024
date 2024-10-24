import numpy as np

import matplotlib.pyplot as plt

def arithmetic_operations():
    
    operation = input("Choose an operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        print(f"Result: {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operation")

def plot_graph():
    x = np.linspace(-10, 10, 400)
    y = eval(input("Enter a function of x (e.g., x**2, np.sin(x)): "))
    
    plt.plot(x, y)
    plt.title("Graph of the function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

def calculate_bmi():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Arithmetic Operations")
        print("2. Plot Graph")
        print("3. Calculate BMI")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            arithmetic_operations()
        elif choice == '2':
            plot_graph()
        elif choice == '3':
            calculate_bmi()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()