 
class Customers:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    def get_name(self):
        return self.name

    def get_membership(self):
        return self.membership

    def set_membership(self, membership):
        self.membership = membership

    def __str__(self):
        return self.name


# 1. Display a message asking the user to enter the name of the customer.
def get_customer_name():
        customer_name = input("Enter the name of the customer: ")
        return customer_name

def get_product_name():
    product_name = input("Enter the name of the product: ")
    return product_name

def get_quantity():
    quantity = input("Enter the quantity: ")
    return quantity

def get_total_cost(product_name, quantity, product_price):
    total_cost = float(quantity) * float(product_price)
    return total_cost

def get_discount(total_cost, membership):
    if membership == "yes":
        discount = total_cost * 0.05
        return discount
    else:
        return 0

def get_final_cost(total_cost, discount):
    final_cost = total_cost - discount
    return final_cost

def display_total_cost(final_cost):
    print("The total cost is $" + str(final_cost))


def get_product_price(product_name):
    return products[product_name]

def get_customer_membership(customer_name):
    membership = input("Does " + customer_name + " have a membership? (y/n): ")
    return membership

def add_customer(customer_name):
    membership = get_customer_membership(customer_name)
    customers[customer_name] = Customers(customer_name, membership)

def display_customers():
    for customer in customers:
        print(customer)

def display_products():
    for product in products:
        print(product)

def display_menu():
    print("\n")
    print("1. Display the list of customers")
    print("2. Display the list of products")
    print("3. Display the total cost")
    print("4. Add a customer")
    print("5. Exit")



products = {"apple": 0.50, "banana": 0.60, "orange": 0.70}
customers = {"John": Customers("John", "yes"), "Mary": Customers("Mary", "no")}


def main():
    customer_name = get_customer_name()
    product_name = get_product_name()
    quantity = get_quantity()
    product_price = products[product_name]
    total_cost = get_total_cost(product_name, quantity, product_price)
    membership = customers[customer_name].get_membership()
    discount = get_discount(total_cost, membership)
    final_cost = get_final_cost(total_cost, discount)
    display_products()
    display_customers()
    display_total_cost(final_cost)
    display_menu(
        customer_name,
        product_name,
        quantity,
        product_price,
        total_cost,
        membership,
        discount,
        final_cost
    )    

    print("\n")
    print("The customer name is: " + customer_name)
    print("The product name is: " + product_name)
    print("The quantity is: " + quantity)
    print("The total cost is: $" + str(final_cost))
