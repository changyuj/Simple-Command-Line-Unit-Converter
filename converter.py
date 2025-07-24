#import tkinter libarary
from tkinter import *

#windows = serves as a container to hold or contain the widgets
#widgets = GUI elements: buttons, textboxes, labels, images

window = Tk() #instantiate an instance of a window
window.geometry("420x400") #size of the window
window.title("Unit Converter") #windows title

label = Label(window, 
              text=" Unit Converter Menu ",
              font=('Arial',20,'bold'),
              relief=RAISED,
              bd=10)
label.pack()

#window.configure(bg="light green") #change background color

window.mainloop() #place windows on computer screen, listen for events




# --- Conversion Functions ---

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    """Converts meters to feet."""
    return meters * 3.28084

def feet_to_meters(feet):
    """Converts feet to meters."""
    return feet / 3.28084

# --- User Interaction Functions ---

def get_float_input(prompt):
    """Helper function to get a float input from the user with basic validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def handle_temperature_conversion():
    """Handles the temperature conversion submenu."""
    while True:
        print("\n--- Temperature Conversion ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Back to Main Menu")
        temp_choice = input("Enter your choice: ")

        if temp_choice == '1':
            c = get_float_input("Enter temperature in Celsius: ")
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C is {f:.2f}°F") # .2f for two decimal places
        elif temp_choice == '2':
            f = get_float_input("Enter temperature in Fahrenheit: ")
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F is {c:.2f}°C") # .2f for two decimal places
        elif temp_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_length_conversion():
    """Handles the length conversion submenu."""
    while True:
        print("\n--- Length Conversion ---")
        print("1. Meters to Feet")
        print("2. Feet to Meters")
        print("3. Back to Main Menu")
        length_choice = input("Enter your choice: ")

        if length_choice == '1':
            m = get_float_input("Enter length in Meters: ")
            f = meters_to_feet(m)
            print(f"{m} meters is {f:.2f} feet") # .2f for two decimal places
        elif length_choice == '2':
            f = get_float_input("Enter length in Feet: ")
            m = feet_to_meters(f)
            print(f"{f} feet is {m:.2f} meters") # .2f for two decimal places
        elif length_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# --- Main Application Logic ---
'''
def main():
    """Main function to run the Unit Converter application."""
    while True:
        print("\n--- Unit Converter Menu ---")
        print("1. Temperature Conversion")
        print("2. Length Conversion")
        print("3. Exit")
        print("---------------------------")

        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            handle_temperature_conversion()
        elif main_choice == '2':
            handle_length_conversion()
        elif main_choice == '3':
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
'''
if __name__ == "__main__":
    main()