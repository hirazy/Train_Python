class Category:
    balance = 0
    list = []

    cgr = ""

    def __init__(self, category):
        self.cgr = category

    def deposit(self, amount, description=""):
        temp = {"amount": amount, "description": description}
        self.list.append(temp)
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.list.append({"amount": amount * -1, "description": description})
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):

        description_Withdraw = "Transfer to " + category.cgr
        description_Deposit = "Transfer from " + self.cgr
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, description_Withdraw)
        category.list.deposit(amount, description_Deposit)
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

    def __str__(self):
        s = self.cgr.center(30, "*") + "\n"

        for item in self.list:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += temp + "\n"

        s += "Total: " + str(self.get_balance())
        return s


def create_spend_chart(categories):
    spend = []
    for category in categories:
        temp = 0
        for item in category.list:
            if item['amount'] < 0:
                temp += abs(item['amount'])
        spend.append(temp)

    total = sum(spend)
    percentage = [i / total * 100 for i in spend]

    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                s += " o "
            else:
                s += "   "
        # Spaces
        s += " "
    s += "\n    ----------"

    cat_length = []
    for category in categories:
        cat_length.append(len(category.cgr))
    max_length = max(cat_length)

    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                s += " " + categories[j].cgr[i] + " "
            else:
                s += "   "
        # Spaces
        s += " "

    return s

if __name__ == '__main__':
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food)
