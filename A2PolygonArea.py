class Rectangle:
    """Calcula y obtiene informacion de un rectangulo"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # Establecer ancho
    def set_width(self, width):
        self.width = width

    # Establecer altura
    def set_height(self, height):
        self.height = height

    # Obtencion del area
    def get_area(self):
        return self.width * self.height

    # Obtencion del perimetro
    def get_perimeter(self):
        return 2*self.width + 2*self.height

    # Obtener diagonal
    def get_diagonal(self):
        return pow(pow(self.width, 2) + pow(self.height, 2), 0.5)

    # Obtener dibujo (representacion)
    def get_picture(self):
        output = ""
        if self.height > 50 or self.width > 50:
            output = "Too big for picture."
            return output
        else:
            for _ in range(0, self.height):
                for _ in range(0, self.width):
                    output += "*"
                output += "\n"
        return output

    def get_amount_inside(self, shape):
        x = int(self.width / shape.width)
        y = int(self.height / shape.height)
        return x * y
# Clase Cuadrado hereda de Rectangulo


class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len, side_len)

    # Obtener medida
    def __str__(self):
        return f"Square(side={self.width})"

    # Establecer lados
    def set_side(self, side_len):
        super().set_width(side_len)
        super().set_height(side_len)


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
