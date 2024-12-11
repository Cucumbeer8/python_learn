class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        return self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:>7.2f}"
            items += f"{desc}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    total = []
    chart = "Percentage spent by category\n"
    for category in categories:
        orders = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        total.append(orders)

    percent = []
    hundred_percent = sum(total)
    for i in range(len(total)):
        percent.append((int(((total[i] / hundred_percent) * 100))) // 10 * 10)

    percentages = []
    if sum(percent) != 100:
        for i in range(len(percent)):
            if percent[i] % 10 >= 5:
                new_percent = (percent[i] // 10 + 1) * 10
            else:
                new_percent = (percent[i] // 10) * 10
            percentages.append(new_percent)
    else:
        percentages = percent

    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += 'o  ' if percent >= i else '   '
        chart += '\n'

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]
    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip('\n')


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(10, 'fuel')
auto.withdraw(20, 'repairs')

print(food)
print(clothing)
print(create_spend_chart([food, clothing, auto]))