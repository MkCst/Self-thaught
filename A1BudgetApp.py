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
            