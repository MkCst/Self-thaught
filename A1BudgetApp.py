class Category:
    def __init__(self, categories):
        self.categories = categories
        self.ledger = []
        self.spent = 0
        self.percent_spent = 0

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
        
