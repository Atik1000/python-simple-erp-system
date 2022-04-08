# In this part, your program can: (a) perform some additional requirements compared to PART 1, and
# (b) be operated using a menu.
# First, compared to the requirements in PART 1, now your program can:
# 1. Display an error message if the product entered by the user does not exist in the product list.
# When this error occurs, the user will be given another chance, until a valid product is entered.
# 2. Display an error message if the product quantity is 0, negative or not an integer. When this
# error occurs, the user will be given another chance, until a valid positive integer quantity is
# entered.
# 3. Display an error message if the answer by the user is not y or n when asking if the customer
# wants a membership. When this error occurs, the user will be given another chance, until a
# valid answer(i.e., y, n) is entered.

# Second, your program will be operated using a menu. A menu-driven program is a computer
# program in which options are offered to the users via the menu. Your program will have the
# following options: place an order, add/update products and prices, display all existing customers,
# display all customers with membership, display all existing products with their prices, exit the
# program(please see Section 5 in this document regarding an example of how the menu program
#         might look like). Below are the specifications of the options:
# Place an order: this option includes all the requirements from 1 to 8 in PART 1 and the
# requirements 1 to 3 in the first part of PART 2.
# 2. Add/update products and prices: this option displays a message asking users to add new
# products or update products, and another message asking users to enter the prices of the
# entered products. The products must be entered as a list that separates by commas, e.g., shirt,
# dress, oven, towel, kettle. The prices will also be entered as a list separating by commas, e.g.,
# 50.0, 60.0, 300.0, 20.0. If the products are new, the products and their prices will be added to
# the data collection of the program. If the products are existing products, the newly entered
# prices will replace existing prices. The order of the prices is the same as the order of the
# products, e.g., in our example, the prices of shirt, dress, oven, and towel are 50, 60, 300, 20
# respectively. A product may have no price, e.g., in our example, kettle does not have any
# price. You can assume the product names are always unique, and each product name is a
# single word with no comma but only alphanumeric characters. You can assume users always
# enter the correct formats of the product and price lists. In this part, you can assume the prices
# entered are always valid and positive numbers and has no comma. And in this part, you can
# also assume users never purchase products with no price.
# 3. Display existing customers: this option displays the names of all existing customers on
# screen.
# 4. Display existing customers with membership: this option displays the names of all customers
# with membership on screen.
# 5. Display existing products: this option displays all the products on screen, with their prices.
# Products with no price will also be displayed.
# 6. Exit the program: this option allows users to exit the program.
# Note that in your program, when a task(option) is accomplished, the menu will appear again for the next

class Customer:
    def __init__(self, name, address, phone, membership):
        self.name = name
        self.address = address
        self.phone = phone
        self.membership = membership

    def __str__(self):
        return self.name + " " + self.address + " " + self.phone + " " + self.membership


# 1. Display an error message if the product entered by the user does not exist in the product list.
# When this error occurs, the user will be given another chance, until a valid product is entered.
# 2. Display an error message if the product quantity is 0, negative or not an integer. When this
# error occurs, the user will be given another chance, until a valid positive integer quantity is
# entered.
# 3. Display an error message if the answer by the user is not y or n when asking if the customer
# wants a membership. When this error occurs, the user will be given another chance, until a
# valid answer(i.e., y, n) is entered.

def add_customer(customer_list, customer_name, customer_address, customer_phone, customer_membership):
    customer_list.append(Customer(customer_name, customer_address, customer_phone, customer_membership))

def add_product(product_list, product_name, product_price):
    product_list.append(product_name)
    product_list.append(product_price)

def display_customer(customer_list):
    for customer in customer_list:
        print(customer)
def display_product(product_list):
    for i in range(0, len(product_list), 2):
        print(product_list[i] + " " + str(product_list[i+1]))
def display_customer_with_membership(customer_list):
    for customer in customer_list:
        if customer.membership == "y":
            print(customer)

def display_product_with_price(product_list):
    for i in range(0, len(product_list), 2):
        if product_list[i+1] != "":
            print(product_list[i] + " " + str(product_list[i+1]))
        else:
            print(product_list[i])


def process_order_with_membership_and_discount():
    product_list = []
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "Eggs", "4.00")
    add_product(product_list, "Cheese", "5.00")
    add_product(product_list, "Butter", "6.00")
    add_product(product_list, "Sugar", "7.00")
    add_product(product_list, "Coffee", "8.00")
    add_product(product_list, "Tea", "9.00")
    add_product(product_list, "Cake", "10.00")
    add_product(product_list, "Cookie", "11.00")
    add_product(product_list, "Candy", "12.00")
    add_product(product_list, "Ice Cream", "13.00")
    add_product(product_list, "Chips", "14.00")
    add_product(product_list, "Pizza", "15.00")
    add_product(product_list, "Burger", "16.00")
    add_product(product_list, "Sandwich", "17.00")
    add_product(product_list, "Salad", "18.00")
    add_product(product_list, "Pancake", "19.00")
    add_product(product_list, "Waffle", "20.00")
    add_product(product_list, "Candy Bar", "21.00")
    add_product(product_list, "Cake", "22.00")
    add_product(product_list, "Cookie", "23.00")
    add_product(product_list, "Candy", "24.00")
    add_product(product_list, "Ice Cream", "25.00")
    add_product(product_list, "Chips", "26.00")
    add_product(product_list, "Pizza", "27.00")

def place_order(customer_list, product_list, customer_name, product_name, product_quantity):
    for customer in customer_list:
        if customer.name == customer_name:
            for i in range(0, len(product_list), 2):
                if product_list[i] == product_name:
                    if product_quantity > 0:
                        if product_quantity <= int(product_list[i+1]):
                            print("Order placed successfully!")
                            product_list[i+1] = str(int(product_list[i+1]) - product_quantity)
                            return
                        else:
                            print("The quantity of the product is not enough!")
                            return
                    else:
                        print("The quantity of the product must be a positive integer!")
                        return
            print("The product does not exist!")
            return
    print("The customer does not exist!")


def process_order_with_membership():
    customer_list = []
    product_list = []
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone: ")
    customer_membership = input("Enter customer membership: ")
    add_customer(customer_list, customer_name, customer_address, customer_phone, customer_membership)
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    product_quantity = input("Enter product quantity: ")
    add_product(product_list, product_name, product_price)
    place_order(customer_list, product_list, customer_name, product_name, product_quantity)



def main():
    customer_list = []
    product_list = []
    while True:
        print("Welcome to the customer management system!")
        print("Please select an option:")
        print("1. Add a customer")
        print("2. Add a product")
        print("3. Display all existing customers")
        print("4. Display all customers with membership")
        print("5. Display all existing products with their prices")
        print("6. Exit the program")
        option = input("Please enter an option: ")
        if option == "1":
            customer_name = input("Please enter the name of the customer: ")
            customer_address = input("Please enter the address of the customer: ")
            customer_phone = input("Please enter the phone number of the customer: ")
            customer_membership = input("Please enter the membership of the customer(y/n): ")
            add_customer(customer_list, customer_name, customer_address, customer_phone, customer_membership)
        elif option == "2":
            product_name = input("Please enter the name of the product: ")
            product_price = input("Please enter the price of the product: ")
            add_product(product_list, product_name, product_price)
        elif option == "3":
            display_customer(customer_list)
        elif option == "4":
            display_customer_with_membership(customer_list)
        elif option == "5":
            display_product_with_price(product_list)
        elif option == "6":
            print("Thank you for using our system!")
            break
        else:
            print("Invalid option!")
        print("")
        print("")

def test_add_customer():
    customer_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    assert customer_list[0].name == "John"
    assert customer_list[0].address == "123 Main St."
    assert customer_list[0].phone == "123-456-7890"
    assert customer_list[0].membership == "n"

def test_add_product():
    product_list = []
    add_product(product_list, "Bread", "2.00")
    assert product_list[0] == "Bread"
    assert product_list[1] == "2.00"

def test_display_customer():
    customer_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    display_customer(customer_list)
    assert customer_list[0].name == "John"
    assert customer_list[0].address == "123 Main St."
    assert customer_list[0].phone == "123-456-7890"
    assert customer_list[0].membership == "n"

def process_order():
    customer_list = []
    product_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_product(product_list, "Bread", "2.00")
    place_order(customer_list, product_list, "John", "Bread", 1)

def test_display_customer_with_membership():
    customer_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_customer(customer_list, "Mary", "456 Main St.", "456-456-7890", "y")
    display_customer_with_membership(customer_list)
    assert customer_list[0].name == "John"
    assert customer_list[0].address == "123 Main St."
    assert customer_list[0].phone == "123-456-7890"
    assert customer_list[0].membership == "n"
    assert customer_list[1].name == "Mary"
    assert customer_list[1].address == "456 Main St."
    assert customer_list[1].phone == "456-456-7890"
    assert customer_list[1].membership == "y"

def test_display_product():
    product_list = []
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    display_product(product_list)
    assert product_list[0] == "Bread"
    assert product_list[1] == "2.00"
    assert product_list[2] == "Milk"
    assert product_list[3] == "3.00"
    assert product_list[4] == ""
    assert product_list[5] == ""

def test_display_product_with_price():
    product_list = []
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    display_product_with_price(product_list)
    assert product_list[0] == "Bread"
    assert product_list[1] == "2.00"
    assert product_list[2] == "Milk"
    assert product_list[3] == "3.00"
    assert product_list[4] == ""
    assert product_list[5] == ""

def test_place_order():
    customer_list = []
    product_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_customer(customer_list, "Mary", "456 Main St.", "456-456-7890", "y")
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    place_order(customer_list, product_list, "John", "Bread", 1)
    assert product_list[0] == "Bread"
    assert product_list[1] == "1"
    assert product_list[2] == "Milk"
    assert product_list[3] == "3.00"
    assert product_list[4] == ""
    assert product_list[5] == ""
    place_order(customer_list, product_list, "Mary", "Milk", 2)
    assert product_list[0] == "Bread"
    assert product_list[1] == "1"
    assert product_list[2] == "Milk"
    assert product_list[3] == "1"
    assert product_list[4] == ""
    assert product_list[5] == ""
    place_order(customer_list, product_list, "Mary", "Bread", 3)
    assert product_list[0] == "Bread"
    assert product_list[1] == "0"
    assert product_list[2] == "Milk"
    assert product_list[3] == "1"
    assert product_list[4] == ""
    assert product_list[5] == ""
    place_order(customer_list, product_list, "John", "Bread", -1)
    assert product_list[0] == "Bread"
    assert product_list[1] == "0"
    assert product_list[2] == "Mil"

def test_process_order():
    customer_list = []
    product_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_customer(customer_list, "Mary", "456 Main St.", "456-456-7890", "y")
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    place_order(customer_list, product_list, "John", "Bread", 1)
    place_order(customer_list, product_list, "Mary", "Milk", 2)
    place_order(customer_list, product_list, "Mary", "Bread", 3)
    process_order(customer_list, product_list)
    assert product_list[0] == "Bread"
    assert product_list[1] == "0"
    assert product_list[2] == "Milk"
    assert product_list[3] == "1"
    assert product_list[4] == ""
    assert product_list[5] == ""

def  test_process_order_with_membership():
    customer_list = []
    product_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_customer(customer_list, "Mary", "456 Main St.", "456-456-7890", "y")
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    place_order(customer_list, product_list, "John", "Bread", 1)
    place_order(customer_list, product_list, "Mary", "Milk", 2)
    place_order(customer_list, product_list, "Mary", "Bread", 3)
    process_order_with_membership(customer_list, product_list)
    assert product_list[0] == "Bread"
    assert product_list[1] == "0"
    assert product_list[2] == "Milk"
    assert product_list[3] == "1"
    assert product_list[4] == ""
    assert product_list[5] == ""

def test_process_order_with_membership_and_discount():
    customer_list = []
    product_list = []
    add_customer(customer_list, "John", "123 Main St.", "123-456-7890", "n")
    add_customer(customer_list, "Mary", "456 Main St.", "456-456-7890", "y")
    add_product(product_list, "Bread", "2.00")
    add_product(product_list, "Milk", "3.00")
    add_product(product_list, "", "")
    place_order(customer_list, product_list, "John", "Bread", 1)
    place_order(customer_list, product_list, "Mary", "Milk", 2)
    place_order(customer_list, product_list, "Mary", "Bread", 3)
    process_order_with_membership_and_discount(customer_list, product_list)
    assert product_list[0] == "Bread"
    assert product_list[1] == "0"
    assert product_list[2] == "Milk"
    assert product_list[3] == "1"
    assert product_list[4] == ""
    assert product_list[5] == ""
