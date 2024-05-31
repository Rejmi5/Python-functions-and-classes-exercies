#-------------------------------------------------------------------------------
#Python Classes - zadania

#Python class, Basic exercises

#1. Write a Python program to import a built-in array module and display the namespace of the said module.
"""
import array

def display_namespace(module):
    print(dir(module))

display_namespace(array)
"""

#2. Write a Python program to create a class and display the namespace of that class.
"""
class MyClass:
    x = 10
    y = 20

    def my_method(self):
        return self.x + self.y

def display_namespace(cls):
    print(cls.__dict__)

display_namespace(MyClass)
"""

#3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
"""
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

instance = MyClass(10, 20)

def display_instance_namespace(instance):
    print(instance.__dict__)

display_instance_namespace(instance)
"""

#4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
#Write a Python program that imports the abs() function using the builtins module, displays the documentation of the abs() function and finds the absolute value of -155.
"""
import builtins

def display_abs_info():
    abs_function = builtins.abs
    print(abs_function.__doc__)
    print(abs_function(-155))

display_abs_info()
"""

#5. Define a Python function student(). Using function attributes display the names of all arguments.
"""
def student(name, age, grade):
    pass

def display_function_attributes(func):
    print(func.__code__.co_varnames)

display_function_attributes(student)
"""

#6. Write a Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
"""
def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    if student_name:
        print(f"Student Name: {student_name}")
    if student_class:
        print(f"Student Class: {student_class}")

student_data(1, "Jan Kowalski", "3A")
"""

#7. Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
"""
class Student:
    student_id = 1
    student_name = "Jan Kowalski"

def display_class_info(cls):
    print(f"Typ klasy: {type(cls)}")
    print(f"Klucze __dict__: {cls.__dict__.keys()}")
    print(f"Wartość __module__: {cls.__module__}")

display_class_info(Student)
"""

#8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.
"""
class Student:
    pass

class Marks:
    pass

def check_instances():
    student_instance = Student()
    marks_instance = Marks()
    print(isinstance(student_instance, Student))
    print(isinstance(marks_instance, Marks))
    print(issubclass(Student, object))
    print(issubclass(Marks, object))

check_instances()
"""

#9. Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
"""
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

def modify_student():
    student = Student("Jan Kowalski", 85)
    print(f"Oryginalne wartości: {student.student_name}, {student.marks}")
    student.student_name = "Anna Nowak"
    student.marks = 90
    print(f"Zmodyfikowane wartości: {student.student_name}, {student.marks}")

modify_student()
"""

#10. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.
"""
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

def modify_attributes():
    student = Student(1, "Jan Kowalski")
    print(student.__dict__)
    student.student_class = "3A"
    print(student.__dict__)
    del student.student_name
    print(student.__dict__)

modify_attributes()
"""

#11. Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class.
"""
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        self.student_class = "3A"
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Student(1, "Jan Kowalski")
student.display_attributes()
"""

#12. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
"""
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

def print_student_attributes():
    student1 = Student(1, "Jan Kowalski")
    student2 = Student(2, "Anna Nowak")

    for student in (student1, student2):
        print(f"Student ID: {student.student_id}")
        print(f"Student Name: {student.student_name}")
        print("-----")

print_student_attributes()
"""

#Python class, Basic application

#1. Write a Python class to convert an integer to a Roman numeral.
"""
class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num):
        result = ""
        for value, numeral in self.value_map:
            while num >= value:
                result += numeral
                num -= value
        return result

converter = IntegerToRoman()
print(converter.convert(3549))  # Output: MMMDXLIX
"""

#2. Write a Python class to convert a Roman numeral to an integer.
"""
class RomanToInteger:
    def __init__(self):
        self.value_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }

    def convert(self, s):
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in self.value_map:
                num += self.value_map[s[i:i+2]]
                i += 2
            else:
                num += self.value_map[s[i]]
                i += 1
        return num

converter = RomanToInteger()
print(converter.convert('MMMDXLIX'))  # Output: 3549
"""

#3. Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
"""
class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if stack == [] or bracket_map[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

validator = ParenthesesValidator()
print(validator.is_valid("()[]{}"))  # Output: True
print(validator.is_valid("([)]"))    # Output: False
"""

#4. Write a Python class to get all possible unique subsets from a set of distinct integers.
#Input : [4, 5, 6]
#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
"""
class UniqueSubsets:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

subset_generator = UniqueSubsets()
print(subset_generator.subsets([4, 5, 6]))
"""

#5. Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#Note: There will be one solution for each input and do not use the same element twice.
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4
#Difficulty: Medium. Company: Google, Facebook
"""
class PairWithTargetSum:
    def find_pair(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            if target - num in num_map:
                return (num_map[target - num], i)
            num_map[num] = i
        return None

finder = PairWithTargetSum()
print(finder.find_pair([10, 20, 10, 40, 50, 60, 70], 50))  # Output: (2, 3)
"""

#6. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]
"""
class ThreeSumZero:
    def find_triplets(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return result

three_sum = ThreeSumZero()
print(three_sum.find_triplets([-25, -10, -7, -3, 2, 4, 8, 10]))
"""

#7. Write a Python class to implement pow(x, n).
"""
class Power:
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

power = Power()
print(power.pow(2, 10))  # Output: 1024
"""

#8. Write a Python class to reverse a string word by word.
#Input string : 'hello .py'
#Expected Output : '.py hello'
"""
class ReverseWords:
    def reverse(self, s):
        return ' '.join(s.split()[::-1])

reverser = ReverseWords()
print(reverser.reverse('hello .py'))  # Output: '.py hello'
"""

#9. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.
"""
class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Wprowadź ciąg znaków: ")

    def print_String(self):
        print(self.string.upper())

manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()
"""

#10. Write a Python class named Rectangle constructed from length and width and a method that will compute the area of a rectangle.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())  # Output: 15
"""

#11. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())       # Output: 78.53981633974483
print(circle.perimeter())  # Output: 31.41592653589793
"""

#12. Write a Python program to get the class name of an instance in Python.
"""
class MyClass:
    pass

def get_class_name(instance):
    return instance.__class__.__name__

obj = MyClass()
print(get_class_name(obj))  # Output: MyClass
"""

#Python class, Real-life problems

#1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
#Sample Employee Data:
#"ADAMS", "E7876", 50000, "ACCOUNTING"
#"JONES", "E7499", 45000, "RESEARCH"
#"MARTIN", "E7900", 50000, "SALES"
#"SMITH", "E7698", 55000, "OPERATIONS"
#Use 'assign_department' method to change the department of an employee.
#Use 'print_employee_details' method to print the details of an employee.
#Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
#overtime = hours_worked - 50
#Overtime amount = (overtime * (salary / 50))
"""
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        overtime = max(0, hours_worked - 50)
        overtime_amount = overtime * (self.emp_salary / 50)
        return self.emp_salary + overtime_amount

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

emp1 = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
emp1.print_employee_details()
print(f"New Salary: {emp1.calculate_emp_salary(55)}")
emp1.emp_assign_department("HR")
emp1.print_employee_details()
"""

#2. Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
#Perform the following tasks now:
#Now add items to the menu.
#Make table reservations.
#Take customer orders.
#Print the menu.
#Print table reservations.
#Print customer orders.
#Note: Use dictionaries and lists to store the data.
"""
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        """
        """
        Dodaje pozycję do menu restauracji.

        Argumenty:
        item_name (str): Nazwa pozycji.
        item_price (float): Cena pozycji.
        """
        """
        self.menu_items[item_name] = item_price

    def book_tables(self, customer_name, table_number):
        """
        """
        Rezerwuje stolik dla klienta.

        Argumenty:
        customer_name (str): Imię klienta.
        table_number (int): Numer stolika.
        """
        """
        self.book_table.append({"customer_name": customer_name, "table_number": table_number})

    def customer_order(self, customer_name, order_items):
        """
        """
        Przyjmuje zamówienie od klienta.

        Argumenty:
        customer_name (str): Imię klienta.
        order_items (list): Lista zamówionych pozycji.
        """
        """
        self.customer_orders.append({"customer_name": customer_name, "order_items": order_items})

    def print_menu(self):
        """
        """
        Wypisuje menu restauracji.
        """
        """
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")

    def print_table_reservations(self):
        """
        """
        Wypisuje rezerwacje stolików.
        """
        """
        print("Table Reservations:")
        for reservation in self.book_table:
            print(f"Customer: {reservation['customer_name']}, Table: {reservation['table_number']}")

    def print_customer_orders(self):
        """
        """
        Wypisuje zamówienia klientów.
        """
        """
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Customer: {order['customer_name']}, Order: {', '.join(order['order_items'])}")

restaurant = Restaurant()
restaurant.add_item_to_menu("Pasta", 12.99)
restaurant.add_item_to_menu("Pizza", 10.99)
restaurant.book_tables("John Doe", 5)
restaurant.customer_order("John Doe", ["Pasta", "Salad"])
restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
"""

#3. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.
"""
class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        """
        """
        Dokonuje wpłaty na konto.

        Argumenty:
        amount (float): Kwota do wpłaty.
        """
        """
        self.balance += amount
        print(f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        """
        Dokonuje wypłaty z konta.

        Argumenty:
        amount (float): Kwota do wypłaty.
        """
        """
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """
        """
        Sprawdza saldo konta.
        """
        """
        print(f"Current balance: ${self.balance:.2f}")

account = BankAccount("123456789", "Alice Smith", 1000.0, "2023-01-01")
account.check_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.check_balance()
"""

#4. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
#Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.
"""
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        """
        """
        Dodaje pozycję do inwentarza.

        Argumenty:
        item_id (str): Identyfikator pozycji.
        item_name (str): Nazwa pozycji.
        stock_count (int): Liczba sztuk w magazynie.
        price (float): Cena pozycji.
        """
        """
        self.items[item_id] = {
            "item_name": item_name,
            "stock_count": stock_count,
            "price": price
        }

    def update_item(self, item_id, stock_count=None, price=None):
        """
        """
        Aktualizuje informacje o pozycji w inwentarzu.

        Argumenty:
        item_id (str): Identyfikator pozycji.
        stock_count (int, opcjonalnie): Zaktualizowana liczba sztuk w magazynie.
        price (float, opcjonalnie): Zaktualizowana cena.
        """
        """
        if item_id in self.items:
            if stock_count is not None:
                self.items[item_id]["stock_count"] = stock_count
            if price is not None:
                self.items[item_id]["price"] = price
        else:
            print(f"Item with ID {item_id} not found.")

    def check_item_details(self, item_id):
        """
        """
        Sprawdza szczegóły pozycji w inwentarzu.

        Argumenty:
        item_id (str): Identyfikator pozycji.

        Zwraca:
        dict: Szczegóły pozycji.
        """
        """
        return self.items.get(item_id, "Item not found")

inventory = Inventory()
inventory.add_item("101", "Laptop", 10, 999.99)
inventory.add_item("102", "Smartphone", 25, 599.99)
inventory.update_item("101", stock_count=8)
inventory.update_item("102", price=579.99)
print(inventory.check_item_details("101"))
print(inventory.check_item_details("102"))
print(inventory.check_item_details("103"))
"""