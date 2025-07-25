#import tkinter libarary
from tkinter import *
from tkinter import messagebox # import messagebox library

#windows = serves as a container to hold or contain the widgets
#widgets = GUI elements: buttons, textboxes, labels, images

result = 0 #global variable

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

def is_number(input_entry):
    """Helper function to check float from the user with basic validation."""
    try:
        float(input_entry) #attempt to convert to float
        return True
    except ValueError:
        return False
'''
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
'''
def handle_temperature_conversion(c_entry, f_entry):
    """Handles the temperature conversion."""
    
    try:
        if c_entry:
            result = celsius_to_fahrenheit(float(c_entry))
            label_temp_result.config(text=f"{c_entry}°C is {result:.2f}°F")
        elif f_entry:
            result = celsius_to_fahrenheit(float(f_entry))
            label_temp_result.config(text=f"{f_entry}°F is {result:.2f}°C")
    except ValueError:
        messagebox.showerror(title='ERROR!',message='Invalid input. Please enter a numerical value.')

'''
    if c_entry:
        #print("celsius is not empty, fahrenheit is empty")
        if is_number(c_entry):
            #print("celsius is a number")
            result = celsius_to_fahrenheit(float(c_entry))
            label_temp_result.config(text=f"{c_entry}°C is {result:.2f}°F")
        else:
            #print("celsius is not a number")
            messagebox.showerror(title='ERROR!',message='Invalid input. Please enter a numerical value.')
    elif f_entry:
        #print("fahrenheit is not empty, celsius is empty")
        if is_number(f_entry):
            #print("celsius is a number")
            result = celsius_to_fahrenheit(float(f_entry))
            label_temp_result.config(text=f"{f_entry}°F is {result:.2f}°C")
        else:
            #print("celsius is not a number")
            messagebox.showerror(title='ERROR!',message='Invalid input. Please enter a numerical value.')
    else:
        #print("both field is not empty")
        messagebox.showerror(title='ERROR!',message='leave one field empty!')
'''

def handle_length_conversion(meter_entry, feet_entry):
    """handles the length conversion."""
    
    try:
        if meter_entry:
            result = meters_to_feet(float(meter_entry))
            label_length_result.config(text=f"{meter_entry} meters is {result:.2f} feet")
        elif feet_entry:
            result = feet_to_meters(float(feet_entry))
            label_length_result.config(text=f"{feet_entry} feet is {result:.2f} meters")
    except ValueError:
        messagebox.showerror(title='ERROR!',message='Invalid input. Please enter a numerical value.')
        label_length_result.config(text="0")
'''
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
'''
def exit_app():
    """Closes the window"""
    print("Exiting Unit Converter. Goodbye!")
    window.destroy()
    
def convert_temp():
    """take input and convert celsius to fahrenheit or vice versa"""
    unit_celsius = entry_celsius.get()
    unit_fahrenheit = entry_fahrenheit.get()

    if not unit_celsius and not unit_fahrenheit: #both field celsius and fahrenheit is empty
        #print("both field celsius and fahrenheit is empty")
        messagebox.showwarning(title='WARNING!',message='No value to convert!')
    elif unit_celsius and unit_fahrenheit:
        #print("both field celsius and fahrenheit has value")
        messagebox.showerror(title='ERROR!', message = 'Both fields has value!')
    else:
        handle_temperature_conversion(unit_celsius, unit_fahrenheit)
        
def convert_length():
    """take input and convert length"""
    unit_meter = entry_meter.get()
    unit_feet = entry_feet.get()
    
    if not unit_meter and not unit_feet:
        messagebox.showwarning(title='WARNING!',message='No value to convert!')
        label_length_result.config(text="0")
    elif unit_meter and unit_feet:
        messagebox.showerror(title='ERROR!', message = 'Both fields has value!')
        label_length_result.config(text="0")
    else:
        handle_length_conversion(unit_meter, unit_feet)

    
# --- Main Application Logic ---

window = Tk() #instantiate an instance of a window
window.geometry("420x550") #size of the window
window.title("Unit Converter") #windows title

label = Label(window, text=" Unit Converter Menu ", font=('Arial',20,'bold'), relief=RAISED, bd=10)
label.pack()

'''button to close the window'''
button = Button(window, text = 'Close Window')
button.config(command=exit_app) #performs call back of function
button.pack(side = BOTTOM)

### temperature conversion ###
'''label and user entry for celsius'''
label_celsius = Label(window, text="Celsius", font=('Arial',15,'bold')) 
label_celsius.place(x=10,y=90)
entry_celsius = Entry(window, bd = 5, font=('Arial',12)) 
entry_celsius.place(x=120,y=90)

'''label and user entry for fahrenheit'''
label_fahrenheit = Label(window, text="Fahrenheit", font=('Arial',15,'bold')) 
label_fahrenheit.place(x=10,y=190)
entry_fahrenheit = Entry(window, bd = 5, font=('Arial',12)) 
entry_fahrenheit.place(x=120,y=190)

'''convert button'''
button_convert = Button(window, text = 'Convert to celcius or fahrenheit', font=('Arial',11,'bold'))
button_convert.config(command=convert_temp)
button_convert.place(x=90,y=135)

'''label to display converted'''
label_temp_result = Label(window,text=result,font=('Arial',13,'bold'), relief=RAISED, bd=3)
label_temp_result.place(x=120,y=230)

### length conversion ###
'''label and user entry for meter'''
label_meter = Label(window, text="Meter", font=('Arial',15,'bold')) 
label_meter.place(x=10,y=300)
entry_meter = Entry(window, bd = 5, font=('Arial',12)) 
entry_meter.place(x=120,y=300)

'''label and user entry for feet'''
label_feet = Label(window, text="Feet", font=('Arial',15,'bold')) 
label_feet.place(x=10,y=400)
entry_feet = Entry(window, bd = 5, font=('Arial',12)) 
entry_feet.place(x=120,y=400)

'''convert button'''
button_convert_length = Button(window, text = 'Convert to Meter or feet', font=('Arial',11,'bold'))
button_convert_length.config(command=convert_length)
button_convert_length.place(x=90,y=350)

'''label to display converted'''
label_length_result = Label(window,text=result,font=('Arial',13,'bold'), relief=RAISED, bd=3)
label_length_result.place(x=120,y=450)


window.mainloop() #place windows on computer screen, listen for events
#print('the program has ended!')

''' command line interface
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

if __name__ == "__main__":
    main()
'''