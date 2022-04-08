# In this part, your program can perform some simple interactions with users (i.e., the cashiers or the store managers):

# 1. Display a message asking the user to enter the name of the customer.
# 2. Display a message asking the user to enter the name of the product the customer chooses. In this part, you can assume the product to be entered is always a valid product.  
# 3. Display a message asking the quantity of the product ordered by the customer that was entered earlier. In this part, you can assume the quantity to be entered is always a positive integer, e.g., 1, 2, 3 …
# 4. Calculate the total cost for the customer including the discount(see No. 5 below).
# 5. For customers with membership, 5% discount will apply. No discount for customers without membership.
# 6. The total cost will be displayed as a formatted message to the user, e.g., "The total cost is $5.00".
# 7. In the program, you should have some lists (or dictionaries or other data types) to store the names of all customers, the names of customers with membership, the available products, the prices of those products. You can assume the customer names and the product names are all unique and case sensitive.
# 8. When a new customer purchases an item, your program will add the customer's name to the customer list. Also, when any customer purchases an item, check if they have a membership;if they currently don't have a membership, display a message asking if they want to have a membership. If yes, then your program will add the customer's name to the customers with membership list. The discount is applied immediately after the customer is added to the customers with membership list. In this part, you can assume the answer entered is always either y or n (meaning yes or no, respectively).
# 9. Note: in the requirements No. 7 & 8, we use the term 'list' when describing the customer list,customer with membership list, etc. But you can use other data types to store this information such as dictionaries and other data types. Make sure you think and analyse the requirements in detail so that you can choose the most appropriate/suitable data types.


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
