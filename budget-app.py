class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    # Calculate total spent and individual category spent amounts
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        total_spent += spent
        category_spent.append(spent)

    # Calculate percentages
    percentages = [int((amount / total_spent) * 100) for amount in category_spent]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Add category names vertically
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart

# Example usage:
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(1000, "initial deposit")
clothing.withdraw(25.55, "shirts")
clothing.withdraw(100, "pants and shoes")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "oil change")
auto.withdraw(50, "parking")

categories = [food, clothing, auto]

print(create_spend_chart(categories))
