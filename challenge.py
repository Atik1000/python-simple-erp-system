
class  Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
        self.total_money = 0
        self.order_history = []
    def add_money(self, money):
        self.total_money += money
    def add_order(self, order):
        self.order_history.append(order)
    def get_total_money(self):
        return self.total_money
    def get_order_history(self):
        return self.order_history
    def get_name(self):
        return self.name
    def get_membership(self):
        return self.membership
    def __str__(self):
        return self.name + " " + self.membership

def  main():
    customer_list = []
    while True:
        print("Welcome to the RMIT Online Shop!")
        print("Please select an option:")
        print("1. Add/update products and prices")
        print("2. Place an order")
        print("3. Display a customer order history")
        print("4. Reveal the most valuable customer")
        print("5. Exit")
        option = input("Please enter your option: ")
        if option == "1":
            print("Please enter the product name and price:")
            while True:
                product_name = input("Product name: ")
                if product_name == "":
                    break
                price = input("Price: ")
                if price == "":
                    break
                try:
                    price = float(price)
                    if price < 0:
                        print("Invalid price!")
                        continue
                except ValueError:
                    print("Invalid price!")
                    continue
                product_list.append(Product(product_name, price))
                print("Product added!")
        elif option == "2":
            print("Please enter the customer name:")
            while True:
                customer_name = input("Customer name: ")
                if customer_name == "":
                    break
                if customer_name in customer_list:
                    break
                else:
                    print("Customer not found!")
                    continue
            print("Please enter the product name and quantity:")
            while True:
                product_name = input("Product name: ")
                if product_name == "":
                    break
                quantity = input("Quantity: ")
                if quantity == "":
                    break
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        print("Invalid quantity!")
                        continue
                except ValueError:
                    print("Invalid quantity!")
                    continue
                for product in product_list:
                    if product.get_name() == product_name:
                        if product.get_price() == 0:
                            print("Product not found!")
                            break
                        else:
                            order = Order(
                                customer_name, product_name, quantity, product.get_price())
                            for customer in customer_list:
                                if customer.get_name() == customer_name:
                                    customer.add_order(order)
                                    customer.add_money(order.get_total_money())
                                    break
                            break
                else:
                    print("Product not found!")
                    continue
        elif option == "3":
            print("Please enter the customer name:")
            while True:
                customer_name = input("Customer name: ")
                if customer_name == "":
                    break
                if customer_name in customer_list:
                    break
                else:
                    print("Customer not found!")
                    continue
            for customer in customer_list:
                if customer.get_name() == customer_name:
                    print("This is the order history of " + customer.get_name() + ":")
                    for order in customer.get_order_history():
                        print(order)
                    break
        elif option == "4":
            print("Please enter the customer name:")
            while True:
                customer_name = input("Customer name: ")
                if customer_name == "":
                    break
                if customer_name in customer_list:
                    break
                else:
                    print("Customer not found!")
                    continue
            max_money = 0
            for customer in customer_list:
                if customer.get_name() == customer_name:
                    if customer.get_total_money() > max_money:
                        max_money = customer.get_total_money()
                        max_customer = customer
            print("The most valuable customer is " + max_customer.get_name() + " with " + str(max_money) + " AUD")
        elif option == "5":
            break
        else:
            print("Invalid option!")

def main_test():
    customer_list = []
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))

def main_test2():
    customer_list = []
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
    customer_list.append(Customer("Jack", "Silver"))
    customer_list.append(Customer("Tom", "Bronze"))
    customer_list.append(Customer("Mary", "Platinum"))
    customer_list.append(Customer("John", "Gold"))
    customer_list.append(Customer("Lily", "Gold"))
