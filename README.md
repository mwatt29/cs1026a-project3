# cs1026a-project3
# What does this Project Do

This project, composed of two Python scripts (car.py and driver.py), focuses on managing cars and drivers in a simulation or management application. It encapsulates the relationship between drivers and cars, enabling the creation, tracking, and manipulation of both entities.

Script: car.py
What This Script Does
The car.py script defines the blueprint for cars and manages attributes and operations specific to a car.

Features
Car Attributes:

Stores essential information about a car, such as:
Make
Model
Year
Mileage
Fuel efficiency (e.g., miles per gallon).
Methods:

Provides operations to:
Track mileage and fuel consumption.
Update or modify car details.
Calculate fuel efficiency for trips or usage.
Reusable Design:

Designed as a class to allow instantiation of multiple car objects with unique attributes.
How to Use
Integration:

Typically used in conjunction with driver.py for combined functionality.
Instantiated and manipulated through the driver-management system.
Standalone Testing:

Can be tested independently by importing the Car class into a test script or directly adding a main method to car.py.
Script: driver.py
What This Script Does
The driver.py script defines the blueprint for drivers and establishes their relationship with cars.

Features
Driver Attributes:

Stores driver information, such as:
Name
Age
License details.
Maintains a record of cars associated with the driver.
Methods:

Assign Cars: Allows associating one or more cars with a driver.
Driver Operations: Tracks trips, updates driving history, or calculates statistics like total miles driven.
Integration with Cars:

Establishes ownership or usage relationships between drivers and cars.
Performs operations involving both drivers and their vehicles.

Technologies/Libraries Used
Language: Python
Core Features:
Object-Oriented Programming (OOP) to define classes and their relationships.
File handling (if applicable, e.g., saving driver or car data).

Skills Demonstrated
OOP Concepts: Encapsulation, relationships between objects, and reusable class designs.
Modular Programming: Separation of car and driver functionalities.
Integration: Simulating real-world relationships and interactions between drivers and vehicles.
