class Category:
    def __init__(self, categories):
        self.categories = categories
        self.ledger = []  # Libro contable o de contabilidad
        self.spent = 0  # Gastos
        self.percent_spent = 0 # Porcentaje de gastos

    def __str__(self):
        categories_length = len(self.categories)
        output_str = ""

        # Primera linea (titulo)
        for _ in range(0, int((30-categories_length)/2)):
            output_str += "*"
        if (categories_length % 2) != 0:
            output_str += "*"
        output_str+=self.categories
        for _ in range(0, int((30-categories_length)/2)):
            output_str += "*"   
        output_str += "\n"
        
        # Descripcion y cantidad
        line = []
        for i in self.ledger:
            line = i["description"][0:23]
            for _ in range(len(line), 23):
                line += " "

            amt = str("{:.2f}".format(i["amount"]))
            for _ in range(0, 7%len(amt)):
                line += " "
            line += amt + "\n"
            output_str += line 
        
        # Balance total de la categoria
        output_str += "Total: "+str(self.get_balance())
        return output_str
        
    # Metodo deposito
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})    
    
    # Metodo retiro
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description": description})
            self.spent += -amount
            return True
        else:
            return False
    
    # Metodo obtener balance
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    # Metodo transferencia
    def transfer(self, amount, budget_dest):
        if self.withdraw(amount, "Transfer to "+ budget_dest.categories):
            budget_dest.deposit(amount, "Transfer from " + self.categories)
            return True
        else:
            return False
    
    # Metodo checar fondos
    def check_funds(self, amount):
        if amount<=self.get_balance():
            return True
        else:
            return False
    
# Metodo creacion de gafico de gastos
def create_spend_chart(categories):
    total_spend = 0
    for i in categories:
        total_spend += i.spent
    for i in categories:
        i.percentage_spent = int(i.spent*100 / total_spend)
    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        output += str(i).rjust(3)+"| "
        for j in categories:
            if j.percentage_spent>=i:
                output += "o  "
            else:
                output += "   "
        output +="\n"

    output +="    -"
    for i in range(0, len(categories)):
        output += "---"
    output += "\n"

    # creacion de lista maximo tamaño de categorias
    max_len_categories = max([len(i.categories) for i in categories])
    
    for i in range(0, max_len_categories):
        output +="     "
        for j in categories:
            if i < len(j.categories):
                output += j.categories[i] + "  "
            else:
                output += "   "
        if i != max_len_categories - 1:
            output += "\n"
    return output
            
if __name__ == '__main__':    
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)
    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))