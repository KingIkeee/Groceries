class Store:
    def __init__(self, name, inventory, distance, is_open = True):
        self.name = name
        self.inventory = inventory
        self.distance = distance
        self.is_open = is_open

    
    def __repr__(self):
        items = ", ".join(self.inventory.keys())
        return f'Welcome to {self.name}! {self.name} has the following items: {items}.'
    
    def is_it_open(self):
        if self.is_open == True:
            return f"{self.name} is open and available for business!"
        else:
            return f"{self.name} is not open right now. Try a different store." 
    
    def is_within_range(self):
        if self.distance <= 5:
            #new_name = self.name
            return f"{self.name} is actually really close! It is {self.distance} miles from you."
        else:
            return f"This store is pretty far from your location. It is {self.distance} miles too far."
        
    def checkout(self, cart):
        total = sum(self.inventory[item] for item in cart if item in self.inventory)
        return f'You have purchased {", ".join(cart)}. Your final total is {total}.'

class Shopper:
    def __init__(self, name, wanted_items, budget):
        self.name = name
        self.wanted_items = wanted_items
        self.budget = budget
        self.final_cart = []
        

    def over_budget(self, store_inventory):
        total_cost = sum(store_inventory[item] for item in self.wanted_items if item in store_inventory)
        if total_cost > self.budget:
            return f"The total of the items in your cart is: {total_cost}. It is way over your budget. Consider another store."
        else:
            return f"Your final total will be {total_cost}. Head over to checkout for purchase."
        
    
    def is_on_list(self, inventory):
        actual_list = [item for item in self.wanted_items if item in inventory]
        return actual_list
    
    def save_list(self, store_name, actual_list):
        saved_list = [actual_list]
        return f"You have saved your shopping list from {store_name}: {", ".join(actual_list)}. It'll be ready for you next week!"

#checkout_list = [Shopper.is_on_list]
#checkout_sum = Shopper.over_budget()

S_S_inv = {"apples": 1.50, "yogurt": 3.50, "banana": 1.75, "eggs": 8, "bread": 7.75, "chicken": 20.25, "waffles": 3.50, "chips":2.50}
Walmart_inv = {"blueberries": 2.50, "cheese": 5.50, "banana": 2, "eggs": 6.50, "bread": 6.50, "chicken": 23.50, "pancakes": 4.50, "crackers": 3.75}
BJ_inv = {"apples": 0.50, "yogurt": 2.75, "banana": 2, "pork": 7, "bread": 4.75, "chicken": 18.25, "waffles": 2.25, "oranges": 3, "ice cream": 6.75}


a = Store("Stop & Shop", S_S_inv, 4)
b = Store("Walmart", Walmart_inv, 3)
c = Store("BJ's", BJ_inv, 6, False)

list_of_available_items = ["apples", "yogurt", "banana", "eggs", "bread", "chicken", "waffles", "chips", "blueberries", "cheese", "pancakes", "crackers", "pork", "oranges", "ice cream"]
shopper_items = []
shopper_name = input("Hello shopper! We heard you are looking to buy some groceries and we want to help you find the right place! Before we begin, we'd like to get your name. What should we call you? ")

print("Excellent " + shopper_name + "! Before we get started with our search, we'd like to know the 5 items you would be looking for! Please select from the following list: " + ", ".join(list_of_available_items))

while len(shopper_items) < 5:
    item = input("Enter an item: ").strip().lower()
    if item in list_of_available_items:
        shopper_items.append(item)
    else:
        print("Sorry, it appears that item is not in the current list. Please select another item.")
print(f"Thank you {shopper_name}! You have selected the following items: {', '.join(shopper_items)}.")
print("Let's see what stores are open and have your items. We found 3 stores in your vacinity.")

choice = input(f"{shopper_name}, the following stores are near you: Stop & Shop, Walmart and BJ's. We suggest picking one that is within 5 miles for the most optimized experience. Please select one of the stores to see if it is open and close enough. ").strip()

selected_store = None
if choice.lower() == "stop & shop":
    selected_store = a
elif choice.lower() == "walmart":
    selected_store = b
elif choice.lower() == "bj's":
    selected_store = c

if selected_store:
    print(selected_store.is_it_open())
    print(selected_store.is_within_range())
else:
    print("Sorry, the store you selected isn't in our database. Please select another store.")

print(f"Great pick {shopper_name}! Hop in we'll take you there right now!")
print(selected_store)

shopper_budget = float(input("One last thing. How much are you willing to spend today for these items? "))

shopper = Shopper(shopper_name, shopper_items, shopper_budget)
available_items = shopper.is_on_list(selected_store.inventory)
print("According to your list, the items that you can buy here are: " + ", ".join(available_items))
print("Let's grab these items and go to checkout.")

total_cost = selected_store.checkout(available_items)
print(total_cost)
budget_status =  shopper.over_budget(selected_store.inventory)
print(budget_status)

choice = input(f"Nice job {shopper_name}! Would you like to save this list for next time? Enter Yes or No! ").strip().lower()
if choice == "yes":
    saved_list_message = shopper.save_list(selected_store.name, available_items)
    print(saved_list_message)
elif choice == "no":
    print("Ok. Hopefully you'll remember for next time.")

print(f"It was a pleasure doing business with you {shopper_name}. Please enjoy your groceries. And again, if you need anymore help, feel free to contact us.")

