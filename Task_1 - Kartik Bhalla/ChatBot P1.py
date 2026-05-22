greeting = {
    "hi": "Hello, what would you like to order today?",
    "hello": "Hello, what would you like to order today?",
    "good morning": "Good morning, what would you like to have today?",
    "take order": "Sure, what would you like to order?",
    "hey": "Hey! What can I get for you today?",
    "hii": "Hi! Ready to place your order?",
    "good afternoon": "Good afternoon! What would you like to order?",
    "good evening": "Good evening! Hungry? What would you like today?",
    "what's up": "Hi! Ready to order something delicious?",
    "how are you": "I'm doing great! What would you like to order today?",
    "can i order": "Of course! What would you like to have?",
    "i want to order": "Sure! Please tell me what you'd like.",
    "order food": "Absolutely! What would you like from the menu?",
    "start order": "Let's get your order started! What would you like?",
    "place order": "Sure! Tell me your order.",
    "hungry": "You've come to the right place! What would you like to eat?",
    "food please": "Sure! What would you like to order?",
    "menu please": "Of course! Here's our menu.",
    "can you take my order": "Absolutely! What would you like?"
}
menu = {
    # Pizza
    "pizza": 120,
    "cheese pizza": 150,
    "veg pizza": 140,
    "paneer pizza": 170,

    # Pasta
    "pasta": 80,
    "white sauce pasta": 100,
    "red sauce pasta": 100,
    "cheese pasta": 120,

    # Main course
    "veg plate": 130,
    "non-veg plate": 200,
    "paneer butter masala": 180,
    "dal makhani": 140,
    "chole bhature": 90,
    "rajma rice": 100,
    "fried rice": 110,
    "veg noodles": 100,
    "chicken biryani": 220,
    "veg biryani": 160,

    # Fast food
    "burger": 40,
    "cheese burger": 70,
    "veg sandwich": 50,
    "grilled sandwich": 80,
    "fries": 60,
    "cheese fries": 90,
    "hot dog": 85,
    "wrap": 100,

    # Snacks
    "samosa": 20,
    "spring roll": 60,
    "garlic bread": 70,
    "nachos": 90,
    "momos": 80,
    "paneer momos": 100,

    # Drinks
    "coke": 30,
    "pepsi": 20,
    "sprite": 30,
    "fanta": 30,
    "cold coffee": 80,
    "milkshake": 100,
    "lemon soda": 40,
    "orange juice": 60,
    "water bottle": 20,

    # Desserts
    "ice cream": 50,
    "brownie": 80,
    "chocolate cake": 120,
    "gulab jamun": 40
}



def process(command):
    reply = greeting.get(command, "Sorry, I didn't understand!")
    print(reply)
    if command in greeting:
        order()

def order():
    bill = 0

    print("\nHere is the Menu:\n")
    for item, price in menu.items():
        print(f"{item.title()} - ₹{price}")
        
    print("\nLet us take your order now.")

    while True:
        item = input("\nOrder Item(type Done to finish): ").lower().strip()
        if item == "done":
            break
        if item not in menu:
            print("Item not present in Menu.\n Sorry for inconvenience.")
            continue
        quantity = int(input("Quantity: "))
        bill += int(menu.get(item)) * quantity
        
            
    print("\nYour order has been placed.")
    print(f"Total bill amount: ₹{bill}")
    print("Thank you for ordering with us!")
    exit()

while True:
    user_input = input("You: ").lower().strip()
    if user_input in ["exit", "bye"]:
        print("Thank you for visiting!")
        break
    process(user_input)