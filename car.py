"""
Murray Watt
mwatt29@uwo.ca
Assignment 04 Problem 01
This program serves as a basic management system for a car rental company,
facilitating the tracking and management of vehicles, customers, 
and rentals through a console-based interface.
"""

class Vehicle:
    _vin_set = set()  # Class variable to ensure VIN uniqueness

    def __init__(self, model, rental_rate, vin, available=True):
        # Initializer for Vehicle objects. Validates VIN, sets model, rental rate, and availability
        self._validate_vin(vin)  # Validates the VIN for uniqueness and format
        self._model = model
        self._rental_rate = rental_rate
        self._available = available

    def _validate_vin(self, vin):
         # Private method to validate the VIN's format and uniqueness
        if len(vin) != 6 or not vin.isalnum():
            raise ValueError("Invalid VIN format. VIN must be a string with 6 characters that can be either digits or letters")
        if vin in self._vin_set:
            raise ValueError("VIN must be unique. Another vehicle with the same VIN already exists.")
        self._vin = vin
        self._vin_set.add(vin) # Adds VIN to the set of existing VINs 

#methods for accessing and modifying the Vehicle's attributes:
    def get_model(self):
        return self._model

    def get_rental_rate(self):
        return self._rental_rate

    def get_vin(self):
        return self._vin

    def get_available(self):
        return self._available

    def set_model(self, model):
        self._model = model

    def set_rental_rate(self, rental_rate):
        self._rental_rate = rental_rate

    def set_available(self, available):
        self._available = available

class Customer:
    def __init__(self, name, phone_number):
         # Initializer for Customer objects. Sets name, phone number, and initializes rented vehicles dictionary
        self._name = name
        self._phone_number = phone_number
        self._rented_vehicles = {} # Dictionary to store rented vehicles

#methods for accessing and modifying the Customer's attributes:
    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_rented_vehicles(self):
        return self._rented_vehicles

    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def add_rented_vehicle(self, vehicle):
         # Adds a vehicle to the customers list of rented vehicles
        self._rented_vehicles[vehicle.get_vin()] = vehicle

    def return_rented_vehicle(self, vin):
        # Removes a vehicle from the customers list of rented vehicles, making it available again
        if vin in self._rented_vehicles:
            self._rented_vehicles[vin].set_available(True)
            del self._rented_vehicles[vin]
            return True
        return False


class Company:
    def __init__(self, name):
         # Initializer for Company objects. Sets name, income, initializes vehicles and customers collections
        self._name = name
        self._income = 0.0
        self._vehicles = {} # Dictionary to store vehicles 
        self._customers = []  # List to store customers

# methods for accessing and modifying the Companys attributes: 
    def get_name(self):
        return self._name

    def get_income(self):
        return self._income

    def get_customers(self):
        return self._customers

    def get_vehicles(self):
        return self._vehicles

    def set_name(self, name):
        self._name = name

    def set_income(self, income):
        self._income = income

    def set_customers(self, customers):
        self._customers = customers

    def set_vehicles(self, vehicles):
        self._vehicles = vehicles

    def add_to_income(self, value):
        # Adds a value to the company's total income
        self._income += value

    def add_vehicle(self, vehicle):
        # Adds a vehicle to the companys dictionary of vehicles
        self._vehicles[vehicle.get_vin()] = vehicle

    def add_customer(self, customer):
         # Adds a customer to the companys list of customers 
        for existing_customer in self._customers:
            if existing_customer.get_name() == customer.get_name():
                return False
        self._customers.append(customer)
        return True

    def rent_vehicle(self, customer_name, vin, rental_duration):
        # Attempts to rent a vehicle to a customer for a specified duration
        customer = next((c for c in self._customers if c.get_name() == customer_name), None)
        vehicle = self._vehicles.get(vin, None)
        if customer and vehicle and vehicle.get_available():
            vehicle.set_available(False)
            revenue = rental_duration * vehicle.get_rental_rate()
            self.add_to_income(revenue)
            customer.add_rented_vehicle(vehicle)
            return True
        return False

    def get_summary(self, file_name):
         # Writes a summary of the companys data to a specified file
        summary = f"Company Name: {self.get_name()}\n"
        summary += f"Total income: {self.get_income()} CAD\n"
        summary += "Customers:\n"
        for customer in self._customers:
            summary += customer.get_name() 
            summary += f" rented {len(customer.get_rented_vehicles())} vehicle(s)\n"
        summary += "Vehicles:\n"
        for vehicle in self._vehicles.values():
            summary += f"{vehicle.get_model()} ({vehicle.get_vin()}),  Available: {vehicle.get_available()}\n"
        summary += "End of Summary"

        with open(file_name, 'w') as file:
            file.write(summary)

# Function to print the user interaction menu
def printMenu():
    print('\n######################')
    print('1: Add new vehicle.')
    print('2: Add new customer.') 
    print('3: Rent vehicle.') 
    print('4: Return rented vehicle.') 
    print('5: Print summary.') 
    print('6: Exit.') 
    print('######################\n')

# Main program function to handle user interactions:
def start():
    company = Company("Pythonic Car Rental Company")
    
    # Pre-added vehicles and customers for demonstration purposes
    company.add_vehicle(Vehicle("Nissan", 10.0, "7bc123"))
    company.add_vehicle(Vehicle("Toyota", 20.0, "7ts123"))
    company.add_vehicle(Vehicle("Tesla", 40.0, "7t0333"))
    
    company.add_customer(Customer("Andleeb", "1234567890"))
    company.add_customer(Customer("Andrew Sagan", "1666567890"))
    company.add_customer(Customer("John Carl", "1666567890"))
    
    while True:
        printMenu()
        choice = input("Enter your choice (1-6): ")
# Handle user input for each menu option:
        if choice == '1':
             # Add a new vehicle workflow
            try:
                model = input("Enter vehicle model: ")
                rental_rate = float(input("Enter rental rate (CAD/day): "))
                vin = input("Enter vehicle VIN: ")
                company.add_vehicle(Vehicle(model, rental_rate, vin))
                print("Vehicle added successfully!")
            except ValueError as e:
                print(e)

        elif choice == '2':
            # Add a new customer workflow
            name = input("Enter customer name: ")
            phone_number = input("Enter phone number: ")
            if not phone_number.isdigit() or len(phone_number) != 10:
                print("Invalid phone number. Phone number must be 10 digits.")
            else:
                customer = Customer(name, phone_number)
                if company.add_customer(customer):
                    print("Customer added successfully.")
                else:
                    print("Customer already exists.")

        elif choice == '3':
            # Rent a vehicle workflow
            customer_name = input("Enter customer name: ")
            vin = input("Enter vehicle VIN: ")
            try:
                rental_duration = int(input("Enter rental duration (days): "))
                if company.rent_vehicle(customer_name, vin, rental_duration):
                    print("Vehicle rented successfully.")
                else:
                    print("Failed to rent the vehicle.")
            except ValueError as e:
                print("Invalid input for rental duration. Please enter a number.")

        elif choice == '4':
             # Return a rented vehicle workflow
            customer_name = input("Enter customer name: ")
            vin = input("Enter vehicle VIN: ")
            customer = next((c for c in company.get_customers() if c.get_name() == customer_name), None)
            if not customer:
                print("Customer not found.")
            else:
                if customer.return_rented_vehicle(vin):
                    print("Vehicle returned successfully.")
                else:
                    print("Failed to return the vehicle.")

        elif choice == '5':
             # Print summary workflow
            file_name = input("Enter file name for summary: ")
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            company.get_summary(file_name)
            print(f"Summary written to {file_name}.")

        elif choice == '6':
            # Exit the program
            print("Exiting the program.")
            break

        else:
            # Handle invalid menu option
            print("Invalid choice. Please enter a number between 1 and 6.")

# Invoke the start function to start the program
start()
